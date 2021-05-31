from ..models import XXECode
from urllib import parse
import urllib.request
from urllib.error import URLError
import concurrent.futures


class XXETestModuleClass:
    DEFAULT_XXE_CHECK_STRING = "Connection refused"

    def __init__(self, host, param_name, request_method='GET'):
        super().__init__()
        if "http" not in host and "https" not in host:
            host = "http://" + host

        self.host = host
        self.param_name = param_name
        self.request_method = request_method

    # XXE request thread. only use xxe module.
    def xxe_test_thread_function(self, xxe_object):
        # tuple [0] = request url, tuple [1] = data
        request_tuple = ()

        request_tuple = (self.host + ('?' if '?' not in self.host else '&') + self.param_name + '='
                         + xxe_object.xxe_code if self.request_method == 'GET' else self.host,
                         parse.urlencode({self.param_name: xxe_object.xxe_code})
                         .encode('utf-8') if self.request_method != 'GET' else None)

        try:
            xxe_test_result = str(urllib.request.urlopen(url=request_tuple[0].replace(" ", "%20"),
                                                         data=request_tuple[1]).read())
            if XXETestModuleClass.DEFAULT_XXE_CHECK_STRING in xxe_test_result:
                return request_tuple[0] if self.request_method == 'GET' else request_tuple[1]

        except URLError:
            return "URL Error occurred. Please check URL or parameter."

        return ''

    def xxe_test(self):
        xxe_test_result = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as xxe_test_executor:
            xxe_test_threads = [xxe_test_executor.submit(self.xxe_test_thread_function, xxe_object)
                                for xxe_object in XXECode.objects.all()]

            for xxe_test_thread in concurrent.futures.as_completed(xxe_test_threads):
                xxe_test_thread_result = xxe_test_thread.result()

                if len(xxe_test_thread_result) > 0:
                    xxe_test_result.append(xxe_test_thread_result)

        return "Possible XXE code: " + ''.join(xxe_test_result) \
            if len(xxe_test_thread_result) > 0 else "Not detect XXE."
