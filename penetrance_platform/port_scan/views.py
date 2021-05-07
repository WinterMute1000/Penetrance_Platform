from django.shortcuts import render
from django.views.generic import CreateView
from .forms import PortScanForm
from .port_scan_module.port_scan_class import PortScanClass


# Create your views here.

class PortScanView(CreateView):
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

        super.__init__()

    def get(self, request, *args, **kwargs):
        context = {'form': PortScanForm()}
        return render(request, "port_scan.html", context)

    def post(self, request, *args, **kwargs):
        port_scanner = PortScanClass.instance()
        form = self.form_class(request.POST)

        if form.is_vaild() and PortScanForm.port_scan_form_validate():
            host = form['hosts']
            # start_port = form['start_port']
            # last_port = form['last_port']
            ports = str(form['start_port']) + "-" + str(form['last_port'])
            scan_method = self.scan_method_dic[form['scan_method']]
            logging = form['logging']

            port_scanner.scan(host, ports, scan_method)
            # Next need logging logic




