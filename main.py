import myinfo

def run_automated_tests(target_url):
    pass

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
    if formatted_whois:
        print(f"Website IP : {formatted_ip_info['ip_address'] if formatted_ip_info else 'N/A'}")
        print(f"Country : {formatted_ip_info['country'] if formatted_ip_info else 'N/A'}")
        print(f"Creation Date : {formatted_whois['creation_date']}")
        print(f"Registry Expiry Date : {formatted_whois['registry_expiry_date']}")
    else:
        print("Website IP and country information not available.")
    run_automated_tests(target_url)
