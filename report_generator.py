from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_report(vulnerabilities, filename="bounty_hunter_report.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, "Bounty Hunter Vulnerability Report")
    c.drawString(100, 730, "=============================")
    
    for i, vuln in enumerate(vulnerabilities, start=1):
        c.drawString(100, 710 - (i * 20), f"{i}. {vuln['name']}: {vuln['description']}")
    
    c.save()
    print(f"Report saved as {filename}")

if __name__ == "__main__":
    vulnerabilities = [
        {"name": "XSS", "description": "Cross-Site Scripting vulnerability detected."},
        {"name": "RCE", "description": "Remote Code Execution vulnerability detected."}
    ]
    generate_report(vulnerabilities)
