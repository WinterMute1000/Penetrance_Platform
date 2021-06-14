from ..models import XSSCode
from urllib import parse
import urllib.request
from urllib.error import URLError
from ...static.test_thread_module import thread_test


class XSSTestModuleClass:
    DEFAULT_XSS_CHECK_STRING = "<xss_test/>"
    IMAGE_BASE_XSS_CHECK_STRING = "<img src=x onerror=alert('XSS');>"

    def __init__(self, host, param_name, request_method='GET'):
        super().__init__()
        if "http" not in host and "https" not in host:
            host = "http://" + host

        self.host = host
        self.param_name = param_name
        self.request_method = request_method

    # XSS request thread. only use xss module.
    def xss_test_thread_function(self, xss_object):
        # tuple [0] = request url, tuple [1] = data
        request_tuple = ()

        request_tuple = (self.host + ('?' if '?' not in self.host else '&') + self.param_name + '='
                         + xss_object.xss_code if self.request_method == 'GET' else self.host,
                         parse.urlencode({self.param_name: xss_object.xss_code})
                         .encode('utf-8') if self.request_method != 'GET' else None)

        try:
            xss_test_result = str(urllib.request.urlopen(url=request_tuple[0].replace(" ", "%20"),
                                                         data=request_tuple[1]).read())
            if XSSTestModuleClass.DEFAULT_XSS_CHECK_STRING in xss_test_result or \
                    XSSTestModuleClass.IMAGE_BASE_XSS_CHECK_STRING in xss_test_result:
                return request_tuple[0] if self.request_method == 'GET' else request_tuple[1]

        except URLError:
            return "URL Error occurred. Please check URL or parameter."

        return ''

    def xss_test(self):
        xss_test_result = thread_test(self.xss_test_thread_function, XSSCode.objects.all())

        return "Possible XSS code: " + ''.join(xss_test_result) \
            if len(xss_test_thread_result) > 0 else "Not detect XSS."
