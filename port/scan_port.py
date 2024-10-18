from theport import scan_ports as theport_scan_ports

def scan_ports(target_ip):
    custom_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 3389, 5432, 5900, 6379, 8080]
    
    open_ports, closed_ports = theport_scan_ports(target_ip, custom_ports)

    with open("port_results.txt", "w") as f:  
        for port, service in open_ports:
            result = f"Port {port} is open: {service}\n"
            print(result.strip())
            f.write(result)

        for port in closed_ports:
            result = f"Port {port} is closed\n"
            print(result.strip())
            f.write(result)

    print("Port scan results saved to port_results.txt.")
