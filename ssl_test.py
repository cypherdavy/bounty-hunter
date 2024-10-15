import ssl
import socket

def test_ssl_security(target_host):
    """Check SSL/TLS security for the target host."""
    try:
        context = ssl.create_default_context()
        with socket.create_connection((target_host, 443)) as conn:
            with context.wrap_socket(conn, server_hostname=target_host) as secure_sock:
                ssl_info = secure_sock.version()
                print(f"SSL/TLS version: {ssl_info}")
    except Exception as e:
        print(f"SSL/TLS Test failed: {e}")
