import requests

def censys_recon(api_id, api_secret, target_ip):
    url = f"https://search.censys.io/api/v2/hosts/{target_ip}"
    headers = {
        'Authorization': f'Basic {api_id}:{api_secret}'
    }
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        print(f"[*] Censys Information for {target_ip}:")
        print(f"IP: {data['ip']}")
        print(f"Services: {data['services']}")
    except Exception as e:
        print(f"Error: {e}")
