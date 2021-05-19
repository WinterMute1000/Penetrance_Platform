import threading
from ..models import XSSCode
import urllib.parse
import urllib.request
import concurrent.futures


class XSSTestModuleClass:
    DEFAULT_XSS_CHECK_STRING = "<xss_test/>"
    IMAGE_BASE_XSS_CHECK_STRING = "<img src=x onerror=alert('XSS');>"

    def __init__(self, host, param_name, request_method='GET'):
        super().__init__()
        if "http" not in host or "https" not in host:
            host = "http://" + host

        self.host = host
        self.param_name = param_name
        self.request_method = request_method

    # XSS request thread. only use xss module.
    def xss_test_thread_function(self):
        # tuple [0] = request url, tuple [1] = data
        request_tuple_list = []
        result_list = []

        for xss_object in XSSCode.objects.all():
            request_tuple_list.append((self.host + '?' + self.param_name + '='
                                       + xss_object.xss_code if self.request_method == 'GET' else self.host,
                                       {self.param_name: xss_object.xss_code} if self.request_method != 'GET'
                                       else None))

        for request_tuple in request_tuple_list:
            xss_test_result = urllib.request.urlopen(url=request_tuple[0], data=request_tuple[1])

            if XSSTestModuleClass.DEFAULT_XSS_CHECK_STRING in xss_test_result.body or \
                    XSSTestModuleClass.IMAGE_BASE_XSS_CHECK_STRING in xss_test_result.body:
                result_list.append(request_tuple[0] if self.request_method == 'GET' else request_tuple[1])

        return "Possible XSS Code: " + ''.join(result_list) if len(result_list) > 0 \
            else "Not detect XSS."

    def xss_test(self):
        with concurrent.futures.ThreadPoolExecutor() as xss_test_executor:
            xss_test_thread = xss_test_executor.submit(self.xss_test_thread_function, self)
            xss_test_result = xss_test_thread.result()

        return xss_test_result

