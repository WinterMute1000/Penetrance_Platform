import nmap
from penetrance_platform.static.singleton_instance import SingletonInstance


# Port scanning class

class PortScanClass(SingletonInstance):
    __instance = None
    port_scanner = nmap.PortScanner()

    def scan(self, hosts, ports="0-65535", arg=""):

        if self.port_scanner is None:
            self.port_scanner = nmap.PortScanner()
        default_scan_arg = "-sV "
        scan_arg = default_scan_arg + arg
        self.port_scanner.scan(hosts=hosts, ports=ports, arguments=scan_arg)

        result = ""
        for host in self.port_scanner.all_hosts():
            result += '----------------------------------------------------\n'
            result += 'Host : %s (%s)' % (host, self.port_scanner[host].hostname()) + "\n"
            result += 'State : %s' % self.port_scanner[host].state() + "\n"
            for proto in self.port_scanner[host].all_protocols():
                result += '----------\n'
                result += 'Protocol : %s' % proto + "\n"

                list_port = self.port_scanner[host][proto].keys()
                list_port.sort()
                for port in list_port:
                    result += 'port : %s    state : %s' % (port, self.port_scanner[host][proto][port]['state']) + "\n"

        return result
