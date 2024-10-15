from ftplib import FTP

def check_ftp_anonymous(host):
    try:
        ftp = FTP(host)
        ftp.login()  # Attempt to log in anonymously
        print(f"Anonymous login successful on {host}")
        ftp.quit()
    except Exception as e:
        print(f"Anonymous login failed on {host}: {e}")

if __name__ == "__main__":
    target_host = input("Enter target FTP host: ")
    check_ftp_anonymous(target_host)
