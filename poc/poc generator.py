def generate_poc(vulnerability, payload, result):
    poc_template = f"""
    Vulnerability: {vulnerability}
    Payload: {payload}
    Result: {result}
    """
    poc_filename = f"{vulnerability}_poc.txt"
    with open(poc_filename, "w") as f:
        f.write(poc_template)
    print(f"PoC saved to {poc_filename}")

if __name__ == "__main__":
    vulnerability = "XSS"
    payload = "<script>alert(1)</script>"
    result = "Alert box popped up"
    generate_poc(vulnerability, payload, result)
    
