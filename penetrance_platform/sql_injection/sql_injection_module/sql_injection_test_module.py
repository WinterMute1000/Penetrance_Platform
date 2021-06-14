from ..models import SQLInjectionCode
from ...static.test_thread_module import thread_test
from urllib import parse
import urllib.request
from urllib.error import URLError


class SQLInjectionTestModuleClass:
    def __init__(self, host, param_name, request_method='GET'):
        super().__init__()
        if "http" not in host and "https" not in host:
            host = "http://" + host

        self.host = host
        self.param_name = param_name
        self.request_method = request_method

    # SQL Injection request thread. only use SQL Injection module.
    def sql_injection_test_thread_function(self, sql_injection_object):
        # tuple [0] = request url(true),tuple[1] = request url(false)
        result_list = []

        # method == 'GET'
        # tuple [0] = request url(true),tuple[1] = request url(false)
        try:
            if self.request_method == 'GET':
                base_url = self.host + ('?' if '?' not in self.host else '&') + self.param_name + '='
                request_tuple = (base_url + sql_injection_object.sql_true_code,
                                 base_url + sql_injection_object.sql_false_code)

                true_response_length = len(urllib.request.urlopen(url=request_tuple[0].replace(" ", "%20")).read())
                false_response_length = len(urllib.request.urlopen(url=request_tuple[1].replace(" ", "%20")).read())

                if true_response_length != false_response_length:
                    return request_tuple[0] + '\n' + request_tuple[1] + '\n\n'
                else:
                    return ''

            # method == 'POST'
            # tuple [0] = true data, tuple[1] = false_data
            else:
                request_tuple = (parse.urlencode({self.param_name: sql_injection_object.sql_true_code}).encode('utf-8'),
                                 parse.urlencode({self.param_name: sql_injection_object.sql_true_code}).encode('utf-8'))

                true_response_length = urllib.request.urlopen(url=self.host, data=request_tuple[0]).read()
                false_response_length = urllib.request.urlopen(url=self.host, data=request_tuple[1]).read()

                if true_response_length != false_response_length:
                    return str(request_tuple[0]).replace('b\'', '') + '\n' + str(request_tuple[1]).replace('b\'', '') \
                           + '\n\n'
                else:
                    return ''

        except URLError:
            return "URL Error occurred. Please check URL or parameter."

    def sql_injection_test(self):

        sql_injection_test_result = thread_test(self.sql_injection_test_thread_function,
                                                SQLInjectionCode.objects.all())

        return "Possible SQL Injection code: " + ''.join(sql_injection_test_result) \
            if len(sql_injection_test_result) > 0 else "Not detect SQL Injection."
