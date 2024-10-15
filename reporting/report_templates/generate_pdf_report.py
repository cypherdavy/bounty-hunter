import os
from fpdf import FPDF
from datetime import datetime

# Function to create a PDF report from scan results
class PDF(FPDF):
    def header(self):
        # Add a logo or title to the header
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Bug Bounty Report', 0, 1, 'C')
        self.ln(10)  # Line break

    def footer(self):
        # Add page number
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln(5)

    def add_section(self, section_title, section_body):
        self.add_page()
        self.chapter_title(section_title)
        self.chapter_body(section_body)

# Function to generate PDF report
def generate_pdf_report(scan_results, report_filename="Bug_Bounty_Report.pdf"):
    # Create PDF object
    pdf = PDF()
    
    # Add title page
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Bug Bounty Report', 0, 1, 'C')
    pdf.set_font('Arial', '', 12)
    pdf.ln(20)
    pdf.cell(0, 10, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 0, 1, 'C')
    pdf.ln(10)

    # Add a section for each scan result
    for section_title, section_body in scan_results.items():
        pdf.add_section(section_title, section_body)
    
    # Save the PDF to file
    pdf.output(report_filename)
    print(f"PDF report generated: {report_filename}")

# Sample scan results (this would be dynamically generated based on actual tool results)
scan_results = {
    "Reconnaissance": "Subdomains discovered: \n- api.example.com \n- dev.example.com \n\nDNS records found: \n- A: 192.168.1.1 \n- CNAME: example.com.",
    "Vulnerability Scanning": "OWASP ZAP scan detected: \n- XSS vulnerability in /login \n- SQL Injection vulnerability in /search.",
    "Exploitation": "Exploit attempted on /admin: \n- Exploited Remote Code Execution vulnerability successfully.",
    "Findings & Recommendations": "The application is vulnerable to Cross-Site Scripting (XSS) and SQL Injection. It is recommended to implement input validation and output encoding."
}

# Generate the report
if __name__ == "__main__":
    generate_pdf_report(scan_results)
