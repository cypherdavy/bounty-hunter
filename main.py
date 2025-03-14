import myinfo
from subdomain import scanner
from port import scan_port
from inclusions import scan
from clickjacking import clickscan
def clean_url(url):
    return url.split("://")[-1].split("/")[0]

def display_whois_info(target_url):
    domain = clean_url(target_url)
    
    whois_info = myinfo.get_whois_info(domain)
    
    if whois_info and 'error' not in whois_info:
        formatted_whois = myinfo.format_whois_info(whois_info)
    else:
        print("Error fetching WHOIS information.")
        formatted_whois = None
    
    ip_address = myinfo.resolve_domain_to_ip(domain)
    if isinstance(ip_address, dict) and 'error' in ip_address:
        print(ip_address['error'])
        formatted_ip_info = None
    else:
        ip_info = myinfo.get_ip_geolocation(ip_address)
        if 'error' in ip_info:
            print("Error fetching IP information.")
            formatted_ip_info = None
        else:
            formatted_ip_info = myinfo.format_ip_info(ip_address, ip_info)

    print("Website info:")
    if formatted_whois and formatted_ip_info:
        print(f"Website IP : {formatted_ip_info.get('ip_address', 'N/A')}")
        print(f"Country : {formatted_ip_info.get('country', 'N/A')}")
        print(f"Creation Date : {formatted_whois.get('creation_date', 'N/A')}")
        print(f"Registry Expiry Date : {formatted_whois.get('registry_expiry_date', 'N/A')}")
    else:
        print("Website IP and country information not available.")

def run_automated_tests(target_url):
    domain = clean_url(target_url)

    print("Scanning subdomains, please wait...")
    user_choice = input("Do you want to scan subdomains? (yes or no) : ").strip().lower()
    if user_choice in ['yes', 'y']:
        scanner.scan_subdomains(domain)
    else:
        print("Skipping subdomain scan.")

    print("Clickjacking scanning, please wait...")
    user_choice = input("Do you want to scan for clickjacking vulnerabilities? (yes or no): ").strip().lower()
    if user_choice in ['yes', 'y']:
        print("Starting clickjacking scan...")
        clickscan.scan(domain)
    else:
        print("Skipping clickjacking scan. Proceeding without scanning for clickjacking vulnerabilities.")

    user_choice = input("Do you want to scan ports? (yes or no) : ").strip().lower()
    if user_choice in ['yes', 'y']:
        print("Scanning ports, please wait...")
        target_ip = myinfo.resolve_domain_to_ip(domain)
        if isinstance(target_ip, dict) and 'error' in target_ip:
            print(target_ip['error'])
            return
        scan_port.scan_ports(target_ip)
    else:
        print("Skipping port scan.")

    user_choice = input("Do you want to scan for inclusion vulnerabilities? (yes or no) : ").strip().lower()
    if user_choice in ['yes', 'y']:
        scan.scan_inclusion(domain)
    else:
        print("Skipping inclusion scan.")

if __name__ == "__main__":
    target_url = input("Enter the target URL : ")
    display_whois_info(target_url)
    run_automated_tests(target_url)
