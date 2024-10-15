import whois

def whois_recon(domain):
    try:
        w = whois.whois(domain)
        print(f"[*] WHOIS Information for {domain}:")
        print(f"Domain Name: {w.domain_name}")
        print(f"Registrar: {w.registrar}")
        print(f"Creation Date: {w.creation_date}")
        print(f"Expiration Date: {w.expiration_date}")
        print(f"Registrant: {w.registrant_name}")
        print(f"Contact Email: {w.emails}")
    except Exception as e:
        print(f"Error: {e}")
