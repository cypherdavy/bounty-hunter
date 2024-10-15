import nmap
import argparse
import sys

def scan_target(target, scan_type, ports=None, intensity=0):
    """Perform different types of Nmap scans on the given target."""
    nm = nmap.PortScanner()
    
    # Scan types and flags
    scan_flags = {
        'syn': '-sS',  # SYN Scan
        'version': '-sV',  # Service Version Detection
        'os': '-O',  # OS Detection
        'udp': '-sU',  # UDP Scan
        'intense': '-T4 -A -v',  # Intense Scan with verbose output
        'quick': '-T4 -F',  # Quick Scan
        'aggressive': '-A'  # Aggressive scan, similar to intense
    }

    if scan_type not in scan_flags:
        print(f"[ERROR] Unknown scan type '{scan_type}'. Available types: {', '.join(scan_flags.keys())}")
        sys.exit(1)

    scan_command = scan_flags[scan_type]

    # Append port options if provided
    if ports:
        scan_command += f" -p {ports}"

    # Intensity customization (only valid for service version detection)
    if scan_type == 'version' and intensity:
        scan_command += f" --version-intensity {intensity}"

    print(f"[INFO] Running Nmap {scan_type} scan on target {target} with options: {scan_command}")

    # Run the Nmap scan
    try:
        nm.scan(hosts=target, arguments=scan_command)

        # Display results
        for host in nm.all_hosts():
            print(f"Host: {host} ({nm[host].hostname()})")
            print(f"State: {nm[host].state()}")

            for proto in nm[host].all_protocols():
                print(f"Protocol: {proto}")
                lport = nm[host][proto].keys()
                for port in sorted(lport):
                    state = nm[host][proto][port]['state']
                    print(f"Port: {port}\tState: {state}")
                    if 'name' in nm[host][proto][port]:
                        print(f"Service: {nm[host][proto][port]['name']}")

    except Exception as e:
        print(f"[ERROR] Failed to execute Nmap scan: {e}")
        sys.exit(1)

def main():
    """Main function to parse arguments and run the Nmap scanner."""
    parser = argparse.ArgumentParser(description="Advanced Nmap Scanner for Bug Bounty.")
    
    # Target and scan type options
    parser.add_argument('target', help="Target IP address or domain name.")
    parser.add_argument('--scan', dest='scan_type', choices=['syn', 'version', 'os', 'udp', 'intense', 'quick', 'aggressive'],
                        default='syn', help="Type of Nmap scan to perform.")
    
    # Optional arguments for ports and version intensity
    parser.add_argument('--ports', '-p', help="Specify a range of ports (e.g., 80,443 or 1-1000).")
    parser.add_argument('--intensity', type=int, default=0, help="Version detection intensity (0-9) for version scans. Default is 0.")
    
    args = parser.parse_args()

    # Run the Nmap scanner based on user input
    scan_target(args.target, args.scan_type, args.ports, args.intensity)

if __name__ == "__main__":
    main()
