from ..models import SQLInjectionCode
from urllib import parse
import urllib.request
from urllib.error import URLError
import concurrent.futures


class SQLInjectionTestModuleClass:
    def __init__(self, host, param_name, request_method='GET'):
        super().__init__()
        if "http" not in host and "https" not in host:
            host = "http://" + host

        self.host = host
        self.param_name = param_name
        self.request_method = request_method

    # SQL Injection request thread. only use SQL Injection module.
    def sql_injection_test_thread_function(self):
        # tuple [0] = request url(true),tuple[1] = request url(false)
        request_tuple_list = []
        result_list = []

        # method == 'GET'
        # tuple [0] = request url(true),tuple[1] = request url(false)
        try:
            if self.request_method == 'GET':
                base_url = self.host + ('?' if '?' not in self.host else '&') + self.param_name + '='
                for sql_injection_object in SQLInjectionCode.objects.all():
                    request_tuple_list.append((base_url + sql_injection_object.sql_true_code,
                                               base_url + sql_injection_object.sql_false_code))

                for request_tuple in request_tuple_list:
                    true_response_length = len(urllib.request.urlopen(url=request_tuple[0].replace(" ", "%20")).read())
                    false_response_length = len(urllib.request.urlopen(url=request_tuple[1].replace(" ", "%20")).read())

                    if true_response_length == false_response_length:
                        result_list.append(request_tuple[0] + '\n' + request_tuple[1] + '\n\n')

            # method == 'POST'
            # tuple [0] = true data, tuple[1] = false_data
            else:
                for sql_injection_object in SQLInjectionCode.objects.all():
                    request_tuple_list.append((parse.urlencode({self.param_name: sql_injection_object.sql_true_code})
                                               .encode('utf-8'),
                                               parse.urlencode({self.param_name: sql_injection_object.sql_true_code})
                                               .encode('utf-8')
                                               ))

                for request_tuple in request_tuple_list:
                    true_response_length = len(urllib.request.urlopen(url=self.host, data=request_tuple[0]).read())
                    false_response_length = len(urllib.request.urlopen(url=self.host, data=request_tuple[1]).read())

                    if true_response_length == false_response_length:
                        result_list.append(str(request_tuple[0]).replace('b\'', '')
                                           + '\n' + str(request_tuple[1]).replace('b\'', '') + '\n\n')

        except URLError:
            return "URL Error occurred. Please check URL or parameter."

        return "Possible SQL Injection Code list \n" + ''.join(result_list) if len(result_list) > 0 \
            else "Not detect SQL Injection."

    def sql_injection_test(self):
        with concurrent.futures.ThreadPoolExecutor() as sql_injection_test_executor:
            sql_injection_test_thread = sql_injection_test_executor.submit(self.sql_injection_test_thread_function)
            sql_injection_test_result = sql_injection_test_thread.result()

        return sql_injection_test_result
