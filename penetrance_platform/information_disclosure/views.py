from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import FormMixin
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .forms import InformationDisclosureForm
from .models import InformationDisclosureLog
import urllib.request


# Create your views here.

class InformationDisclosureView(CreateView):
    form_class = InformationDisclosureForm

    def get(self, request, *args, **kwargs):
        context = {'form': InformationDisclosureForm()}

        information_disclosure_template = loader.get_template('information_disclosure.html')
        return HttpResponse(information_disclosure_template.render(context, request))

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            host = form.data['host']
            logging = form.data['logging']

            host_headers = urllib.request.urlopen(url=host).info()
            version_info = ""
            x_powered_by = ""
            if "Server" in host_headers.keys():
                version_info = str(host_headers['Server'])

            if "X-Powered-By" in host_headers.keys():
                x_powered_by = str(host_headers['X-Powered-By'])

            result = version_info + "\n" + x_powered_by

            if logging:
                information_disclosure_log = InformationDisclosureLog.objects.create(host=host,
                                                                                     result=result)
                information_disclosure_log.save()

            return JsonResponse({'result': result}, json_dumps_params={'ensure_ascii': True})

        return JsonResponse({'result': "Invalid host"}, json_dumps_params={'ensure_ascii': True})





