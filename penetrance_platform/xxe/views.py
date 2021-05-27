# from django.shortcuts import render
from django.views.generic import CreateView
# from django.views.generic.edit import FormMixin
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .forms import XXEForm
from .models import XXELog
from .xxe_module.xxe_test_module import XXETestModuleClass


# Create your views here.

class XXEView(CreateView):
    form_class = XXEForm

    def get(self, request, *args, **kwargs):
        context = {'form': XXEForm()}

        xxe_template = loader.get_template('xxe.html')
        return HttpResponse(xxe_template.render(context, request))

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            host = form.data['host']
            param_name = form.data['param_name']
            logging = form.data['logging']
            method = form.data['method']

            xxe_test_module = XXETestModuleClass(host, param_name, method)
            xxe_test_result = xxe_test_module.xxe_test()

            if logging:
                xxe_log = XXELog.objects.create(host=host, xss_code=xxe_test_result,
                                                result=True if "Not detect XXE." not in xxe_test_result else False)
                xxe_log.save()

            return JsonResponse({'result': xxe_test_result}, json_dumps_params={'ensure_ascii': True})

        return JsonResponse({'result': "Invalid host"}, json_dumps_params={'ensure_ascii': True})
