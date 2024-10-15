import requests

def test_reflected_xss(url):
    payload = "<script>alert('XSS')</script>"
    params = {'search': payload}  # Modify based on the target param
    try:
        response = requests.get(url, params=params)
        if payload in response.text:
            print(f"[+] Reflected XSS vulnerability found on {url}")
        else:
            print("[-] No Reflected XSS detected")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target_url = input("Enter target URL: ")
    test_reflected_xss(target_url)
