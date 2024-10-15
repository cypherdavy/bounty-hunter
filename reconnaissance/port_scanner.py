# port_scanner.py
import socket
import threading
from queue import Queue

# Number of threads to speed up scanning
num_threads = 100

# List of common ports to scan
common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 8080, 3306, 1433, 1521, 3389, 5900]

# Queue for port numbers
queue = Queue()

# Lock for printing results without overlap
print_lock = threading.Lock()

def banner_grab(ip, port):
    """Function to perform simple banner grabbing for service identification."""
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        banner = s.recv(1024).decode().strip()
        return banner
    except:
        return None
    finally:
        s.close()

def port_scan(ip):
    """Function to scan individual ports."""
    while not queue.empty():
        port = queue.get()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                with print_lock:
                    print(f"[+] Port {port} is open")
                    banner = banner_grab(ip, port)
                    if banner:
                        print(f"    Service: {banner}")
            sock.close()
        except Exception as e:
            with print_lock:
                print(f"Error scanning port {port}: {e}")
        queue.task_done()

def main(target_ip, ports=None):
    if ports is None:
        ports = common_ports
    else:
        ports = list(map(int, ports.split(',')))

    print(f"Scanning {target_ip} for open ports...")

    for port in ports:
        queue.put(port)

    # Start multiple threads
    for _ in range(num_threads):
        thread = threading.Thread(target=port_scan, args=(target_ip,))
        thread.daemon = True
        thread.start()

    queue.join()

if __name__ == "__main__":
    target = input("Enter the target IP address: ")
    ports_to_scan = input("Enter a comma-separated list of ports to scan (press Enter for common ports): ")

    main(target, ports_to_scan)
