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
    def xxe_test_thread_function(self):
        # tuple [0] = request url, tuple [1] = data
        request_tuple_list = []
        result_list = []

        for xxe_object in XXECode.objects.all():
            request_tuple_list.append((self.host + ('?' if '?' not in self.host else '&') + self.param_name + '='
                                       + xxe_object.xxe_code if self.request_method == 'GET' else self.host,
                                       parse.urlencode({self.param_name: xxe_object.xxe_code})
                                       .encode('utf-8') if self.request_method != 'GET' else None))

        for request_tuple in request_tuple_list:
            try:
                xxe_test_result = str(urllib.request.urlopen(url=request_tuple[0].replace(" ", "%20"),
                                                             data=request_tuple[1]).read())
                if XXETestModuleClass.DEFAULT_XXE_CHECK_STRING in xxe_test_result:
                    result_list.append(request_tuple[0] if self.request_method == 'GET' else request_tuple[1])

            except URLError:
                return "URL Error occurred. Please check URL or parameter."

        return "Possible XXE Code: " + ''.join(result_list) if len(result_list) > 0 \
            else "Not detect XXE."

    def xxe_test(self):
        with concurrent.futures.ThreadPoolExecutor() as xxe_test_executor:
            xxe_test_thread = xxe_test_executor.submit(self.xxe_test_thread_function)
            xxe_test_result = xxe_test_thread.result()

        return xxe_test_result
