import requests

def subdomain_brute(domain, wordlist):
    with open(wordlist, 'r') as file:
        for subdomain in file:
            subdomain = subdomain.strip()
            url = f"http://{subdomain}.{domain}"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print(f"[+] Found Subdomain: {url}")
            except requests.exceptions.RequestException:
                continue
