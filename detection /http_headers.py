import requests

def http_headers_analysis(url):
    try:
        response = requests.get(url)
        headers = response.headers

        print(f"[+] HTTP Headers for {url}:")
        for header, value in headers.items():
            print(f"  - {header}: {value}")

        if 'Server' in headers:
            print(f"[+] Web Server: {headers['Server']}")
        if 'X-Powered-By' in headers:
            print(f"[+] Technology: {headers['X-Powered-By']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
