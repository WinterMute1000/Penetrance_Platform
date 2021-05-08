from django import forms

# Need host,ports,scan method,and datalog
SCAN_METHOD = (
    (1, "TCP SYN scan"),
    (2, "TCP connect scan"),
    (3, "PING scan"),
    (4, "ACK scan"),
    (5, "RPC scan"),
    (6, "UDP scan"),
    (7, "FIN scan"),
    (8, "Xmas scan"),
    (9, "Null scan"),
)


class PortScanForm(forms.Form):
    host = forms.CharField(required=True, help_text="Input host address or domain name")
    start_port = forms.IntegerField(required=False, help_text="Input start port. Default:0")
    last_port = forms.IntegerField(required=False, help_text="Input last port default:1024")
    scan_method = forms.ChoiceField(required=True, choices=SCAN_METHOD,
                                    help_text="Choice scanning method")
    logging = forms.BooleanField(required=True, help_text="Check if you want logging.")

    @staticmethod
    def port_scan_form_validate(form):
        host = form.get['host']
        start_port = form.get['start_port']
        last_port = form.get['last_port']
        scan_method = form.get['scan_method']

        if start_port is None:
            pass
        elif start_port > 65535 or start_port < 0:
            return False

        if last_port is None:
            pass
        elif last_port > 65535 or last_port < 0 or last_port < start_port:
            return False

        if scan_method > 9 or scan_method < 1:
            return False

        if len(host) > 2048 or host is None:
            return False
