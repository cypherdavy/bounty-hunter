import requests

def fuzz_http_headers(target_url, headers_to_fuzz):
    """Fuzz HTTP headers to find potential vulnerabilities."""
    try:
        for header, value in headers_to_fuzz.items():
            response = requests.get(target_url, headers={header: value})
            if response.status_code != 200:
                print(f"Potential vulnerability detected with header {header}: {value}")
    except Exception as e:
        print(f"Error during HTTP header fuzzing: {e}")
