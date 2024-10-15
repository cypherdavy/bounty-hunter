import os

def sql_injection_scan(url):
    command = f"sqlmap -u {url} --batch"
    os.system(command)

if __name__ == "__main__":
    target_url = input("Enter the target URL for SQL Injection scan: ")
    sql_injection_scan(target_url)
