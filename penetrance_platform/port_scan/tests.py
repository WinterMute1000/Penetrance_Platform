from django.test import TestCase
from .models import PortScanLog
from .port_scan_module.port_scan_class import PortScanClass
from .forms import PortScanForm


# Create your tests here.

class PortScanTest(TestCase):

    def test_default_scan(self):
        test_scanner = PortScanClass.instance()
        print(test_scanner.scan("127.0.0.1", arg="-sS"))
        test_form = PortScanForm(data={'host': "127.0.0.1", 'scan_method': 1, 'logging': False})

        self.assertIs(PortScanForm.port_scan_form_validate(test_form), True)

    def test_start_port_under_zero(self):
        test_form = PortScanForm(data={'host': '127.0.0.1', 'start_port': -1,
                                       'last_port': 65535, 'scan_method': 1, 'logging': False})
        self.assertIs(PortScanForm.port_scan_form_validate(test_form), False)

    def test_start_port_over_max_port(self):
        test_form = PortScanForm(data={'host': '127.0.0.1', 'start_port': 65536,
                                       'last_port': 3000, 'scan_method': 1, 'logging': False})
        self.assertIs(PortScanForm.port_scan_form_validate(test_form), False)

    def test_last_port_under_zero(self):
        test_form = PortScanForm(data={'host': '127.0.0.1', 'start_port': 22,
                                       'last_port': -1, 'scan_method': 1, 'logging': False})
        self.assertIs(PortScanForm.port_scan_form_validate(test_form), False)

    def test_last_port_over_max_port(self):
        test_form = PortScanForm(data={'host': '127.0.0.1', 'start_port': 0,
                                       'last_port': 65536, 'scan_method': 1, 'logging': False})
        self.assertIs(PortScanForm.port_scan_form_validate(test_form), False)

    def test_last_port_under_first_port(self):
        test_form = PortScanForm(data={'host': '127.0.0.1', 'start_port': 25,
                                       'last_port': 23, 'scan_method': 1, 'logging': False})
        self.assertIs(PortScanForm.port_scan_form_validate(test_form), False)

    def test_not_validate_scan_method(self):
        test_form = PortScanForm(data={'host': '127.0.0.1', 'start_port': 0,
                                       'last_port': 65535, 'scan_method': 0, 'logging': False})
        self.assertIs(PortScanForm.port_scan_form_validate(test_form), False)
        test_form = PortScanForm(data={'host': '127.0.0.1', 'start_port': 0,
                                       'last_port': 65535, 'scan_method': 10, 'logging': False})
        self.assertIs(PortScanForm.port_scan_form_validate(test_form), False)

    def test_host_over_max_len(self):
        test_form = PortScanForm(data={'host': 'a'*2049, 'start_port': 0,
                                       'last_port': 65535, 'scan_method': 1, 'logging': False})
        self.assertIs(PortScanForm.port_scan_form_validate(test_form), False)
