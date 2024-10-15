import dns.resolver

def dns_recon(domain):
    try:
        # Query for A records (IP addresses)
        a_records = dns.resolver.resolve(domain, 'A')
        print(f"[*] A Records:")
        for ip in a_records:
            print(ip.to_text())
        
        # Query for MX records (Mail Servers)
        mx_records = dns.resolver.resolve(domain, 'MX')
        print(f"[*] MX Records:")
        for mail_server in mx_records:
            print(mail_server.to_text())
        
        # Query for NS records (Name Servers)
        ns_records = dns.resolver.resolve(domain, 'NS')
        print(f"[*] NS Records:")
        for nameserver in ns_records:
            print(nameserver.to_text())
    
    except Exception as e:
        print(f"Error: {e}")
