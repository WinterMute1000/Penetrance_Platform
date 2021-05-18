import threading
from ..models import XSSCode
import urllib.parse
import urllib.request


class XSSModule:
    # XSS request thread. only use xss module.
    class XSSRequestThread(threading.Thread):
        def __init__(self, host, param_name, request_method='GET'):
            super().__init__()
            if "http" not in host or "https" not in host:
                host = "http://" + host

            self.host = host
            self.param_name = param_name
            self.request_method = request_method

        def run(self):
            # tuple [0] = request url, tuple [1] = data
            request_tuple_list = []

            for xss_object in XSSCode.objects.all():
                request_tuple_list.append((self.host + '?' + self.param_name + '='
                                           + xss_object.xss_code if self.request_method == 'GET' else self.host,
                                           {self.param_name: xss_object.xss_code} if self.request_method != 'GET'
                                           else None))

            for request_tuple in request_tuple_list:
                urllib.request.urlopen(url=request_tuple[0], data=request_tuple[1])

    def xss_test(self, host, arg_name, request_method='GET'):
        xss_request_thread = self.XSSRequestThread(host, arg_name, request_method)
        xss_request_thread.start()
