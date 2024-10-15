import requests
import json

# Function to interact with BuiltWith API
def builtwith_detect(url):
    api_url = f"https://api.builtwith.com/v12/api.json?KEY=YOUR_BUILTWITH_API_KEY&LOOKUP={url}"
    try:
        response = requests.get(api_url)
        result = response.json()

        if response.status_code == 200:
            print(f"[+] Technologies detected on {url}:")
            for tech in result['Results'][0]['Result']['Paths']:
                print(f"  - {tech['Path']}: {tech['Name']}")
        else:
            print("[-] Error fetching BuiltWith data.")
    except Exception as e:
        print(f"Error: {e}")
