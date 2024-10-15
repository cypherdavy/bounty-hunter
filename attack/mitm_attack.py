import requests

def mitm_attack(target_url):
    """Perform a basic Man-in-the-Middle (MITM) attack using a proxy."""
    proxies = {
        'http': 'http://localhost:8080',
        'https': 'http://localhost:8080'
    }
    
    try:
        response = requests.get(target_url, proxies=proxies)
        if response.status_code == 200:
            print(f"MITM attack successful, intercepted response: {response.text}")
            return True
        else:
            print("MITM attack failed.")
            return False
    except Exception as e:
        print(f"Error during MITM attack: {e}")
        return False
