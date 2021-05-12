from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import FormMixin
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .forms import PortScanForm
from .port_scan_module.port_scan_class import PortScanClass
from .models import PortScanLog


# Create your views here.

class PortScanView(CreateView):
    form_class = PortScanForm

    def __init__(self):
        self.scan_method_dic = {
            1: "-sS",
            2: "-sT",
            3: "-sP",
            4: "-sA",
            5: "-sR",
            6: "-sU",
            7: "-sF",
            8: "-sX",
            9: "-sN",
        }

        super(PortScanView, self).__init__()

    def get(self, request, *args, **kwargs):
        context = {'form': PortScanForm()}

        port_scan_template = loader.get_template('port_scan.html')
        return HttpResponse(port_scan_template.render(context, request))

    def post(self, request, *args, **kwargs):
        port_scanner = PortScanClass()
        form = self.form_class(request.POST)
        print(form)

        if form.is_valid():
            host = form['hosts']
            start_port = form['start_port']
            last_port = form['last_port']

            if start_port is None:
                start_port = 0
            if last_port is None:
                last_port = 1024

            ports = str(start_port) + "-" + str(last_port)
            scan_method = self.scan_method_dic[form['scan_method']]
            logging = form['logging']

            result = port_scanner.scan(host, ports, scan_method)
            # logging logic

            if logging:
                port_scan_log = PortScanLog.objects.create(host=host, result=result)
                port_scan_log.save()

        return JsonResponse({'result': result}, json_dumps_params={'ensure_ascii': True})
