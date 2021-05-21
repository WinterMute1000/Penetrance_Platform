# from django.shortcuts import render
from django.views.generic import CreateView
# from django.views.generic.edit import FormMixin
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .forms import XSSForm
from .models import XSSLog
from .xss_module.xss_test_module import XSSTestModuleClass


# Create your views here.

class XSSView(CreateView):
    form_class = XSSForm

    def get(self, request, *args, **kwargs):
        context = {'form': XSSForm()}

        xss_template = loader.get_template('xss.html')
        return HttpResponse(xss_template.render(context, request))

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            host = form.data['host']
            param_name = form.data['param_name']
            logging = form.data['logging']
            method = form.data['method']

            xss_test_module = XSSTestModuleClass(host, param_name, method)
            xss_test_result = xss_test_module.xss_test()

            if logging:
                xss_log = XSSLog.objects.create(host=host, xss_code=xss_test_result,
                                                result=True if "Not detect XSS." not in xss_test_result else False)
                xss_log.save()

            return JsonResponse({'result': xss_test_result}, json_dumps_params={'ensure_ascii': True})

        return JsonResponse({'result': "Invalid host"}, json_dumps_params={'ensure_ascii': True})
