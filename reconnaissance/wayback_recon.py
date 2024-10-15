import requests

def wayback_snapshot(url):
    api_url = f"http://archive.org/wayback/available?url={url}"
    try:
        response = requests.get(api_url)
        data = response.json()
        if data['archived_snapshots']:
            snapshot = data['archived_snapshots']['closest']
            print(f"[*] Wayback Snapshot Found: {snapshot['url']}")
        else:
            print("[-] No Wayback Snapshot found.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
