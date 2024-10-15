import requests

def netcraft_detect(url):
    try:
        api_url = f"https://api.netcraft.com/?url={url}"
        response = requests.get(api_url)

        if response.status_code == 200:
            print(f"[+] Netcraft data for {url}:")
            print(f"  - {response.text}")
        else:
            print("[-] Error fetching Netcraft data.")
    except Exception as e:
        print(f"Error: {e}")
