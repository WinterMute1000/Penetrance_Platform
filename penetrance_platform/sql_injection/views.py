# from django.shortcuts import render
from django.views.generic import CreateView
# from django.views.generic.edit import FormMixin
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .forms import SQLInjectionForm
from .models import SQLInjectionLog
from .sql_injection_module.sql_injection_test_module import SQLInjectionTestModuleClass


# Create your views here.

class SQLInjectionView(CreateView):
    form_class = SQLInjectionForm

    def get(self, request, *args, **kwargs):
        context = {'form': SQLInjectionForm()}

        xss_template = loader.get_template('sql_injection.html')
        return HttpResponse(xss_template.render(context, request))

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            host = form.data['host']
            param_name = form.data['param_name']
            logging = form.data['logging']
            method = form.data['method']

            sql_injection_test_module = SQLInjectionTestModuleClass(host, param_name, method)
            sql_injection_test_result = sql_injection_test_module.sql_injection_test()

            if logging:
                sql_injection_log = SQLInjectionLog.objects.create(host=host,
                                                                   sql_injection_code=sql_injection_test_result,
                                                                   result=True if "Not detect SQL Injection." \
                                                                   not in sql_injection_test_result else False)
                sql_injection_log.save()

            return JsonResponse({'result': sql_injection_test_result}, json_dumps_params={'ensure_ascii': True})

        return JsonResponse({'result': "Invalid host"}, json_dumps_params={'ensure_ascii': True})
