import ssl
import socket
import OpenSSL

def ssl_recon(domain):
    try:
        context = ssl.create_default_context()
        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=domain)
        conn.connect((domain, 443))
        cert = conn.getpeercert()
        print(f"[*] SSL Certificate Information for {domain}:")
        print(f"Issuer: {cert['issuer']}")
        print(f"Subject: {cert['subject']}")
        print(f"Not Before: {cert['notBefore']}")
        print(f"Not After: {cert['notAfter']}")
    except Exception as e:
        print(f"Error: {e}")
