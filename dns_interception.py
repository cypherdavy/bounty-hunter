import dns.resolver

def dns_interception(domain):
    """Perform DNS interception to find potential issues like subdomain hijacking."""
    try:
        result = dns.resolver.resolve(domain, 'A')
        ip_addresses = [ip.address for ip in result]
        print(f"IP addresses for {domain}: {ip_addresses}")
        return ip_addresses
    except dns.resolver.NoAnswer as e:
        print(f"No DNS record found for {domain}: {e}")
        return []
