import requests

def fuzz_sql_injection(target_url, payloads):
    """Fuzz SQL injection parameters with a list of common payloads."""
    for payload in payloads:
        response = requests.get(target_url, params={"input": payload})
        if "syntax error" in response.text or "mysql" in response.text:
            print(f"Potential SQL Injection found with payload: {payload}")
