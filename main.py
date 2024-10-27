import myinfo
from subdomain import scanner
from port import scan_port
from inclusion import scan_inclusion  

def run_automated_tests(target_url):
    print("Scanning subdomains, please wait...")
    user_choice = input("Do you want to scan subdomains? (yes or no): ").strip().lower()
    if user_choice in ['yes', 'y']:
        scanner.scan_subdomains(target_url)
    else:
        print("Skipping subdomain scan.")

    user_choice = input("Do you want to scan ports? (yes or no): ").strip().lower()
    if user_choice in ['yes', 'y']:
        print("Scanning ports, please wait...")
        target_ip = myinfo.resolve_domain_to_ip(target_url) 
        if isinstance(target_ip, dict) and 'error' in target_ip:
            print(target_ip['error'])
            return  
        scan_port.scan_ports(target_ip) 
    else:
        print("Skipping port scan.")

    user_choice = input("Do you want to scan for inclusion vulnerabilities? (yes or no): ").strip().lower()
    if user_choice in ['yes', 'y']:
        scan_inclusion(target_url) 
    else:
        print("Skipping inclusion scan.") 

if __name__ == "__main__":
    target_url = input("Enter the target URL: ")
    whois_info = myinfo.get_whois_info(target_url)
    if 'error' not in whois_info:
        formatted_whois = myinfo.format_whois_info(whois_info)
    else:
        print("Error fetching WHOIS information.")
        formatted_whois = None
    
    ip_address = myinfo.resolve_domain_to_ip(target_url)
    if isinstance(ip_address, dict) and 'error' in ip_address:
        print(ip_address['error'])
    else:
        ip_info = myinfo.get_ip_geolocation(ip_address)
        if 'error' in ip_info:
            print("Error fetching IP information.")
            formatted_ip_info = None
        else:
            formatted_ip_info = myinfo.format_ip_info(ip_address, ip_info)

    print("Website info:")
    if formatted_whois and formatted_ip_info:
        print(f"Website IP: {formatted_ip_info['ip_address']}")
        print(f"Country: {formatted_ip_info['country']}")
        print(f"Creation Date: {formatted_whois['creation_date']}")
        print(f"Registry Expiry Date: {formatted_whois['registry_expiry_date']}")
    else:
        print("Website IP and country information not available.")

    run_automated_tests(target_url)
