import ssl
import socket

def check_ssl_cert(target):
    try:
        port = 443
        context = ssl.create_default_context()
        with socket.create_connection((target, port)) as sock:
            with context.wrap_socket(sock, server_hostname=target) as ssock:
                cert = ssock.getpeercert()
                print(f"SSL Certificate for {target}:")
                for key, value in cert.items():
                    print(f"{key}: {value}")
    except Exception as e:
        print(f"Error checking SSL certificate: {e}")

if __name__ == "__main__":
    target = input("Enter target domain: ")
    check_ssl_cert(target)
