import vulheader

def print_vulnerability(header, status):
    print(f"{header}: {'Missing' if status == 'missing' else 'Present'}")

def scan_iframe(target_url):
    result = vulheader.check(target_url, "X-Frame-Options")
    print_vulnerability("X-Frame-Options", result)
