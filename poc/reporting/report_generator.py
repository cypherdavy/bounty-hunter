import os
from fpdf import FPDF
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

class ReportGenerator:
    def __init__(self, output_dir="reports"):
        self.output_dir = output_dir
        self.create_output_directory()

    def create_output_directory(self):
        """Create the directory to store the reports if it doesn't exist."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_html_report(self, scan_results, report_filename="bug_bounty_report.html"):
        """Generate an HTML report from the scan results."""
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('report_template.html')

        # Generate the HTML content using the template
        html_content = template.render(scan_results=scan_results, generated_on=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        # Write the HTML content to a file
        with open(os.path.join(self.output_dir, report_filename), 'w') as file:
            file.write(html_content)

        print(f"HTML report generated: {os.path.join(self.output_dir, report_filename)}")

    def generate_pdf_report(self, scan_results, report_filename="bug_bounty_report.pdf"):
        """Generate a PDF report from the scan results."""
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        
        # Add title page
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, 'Bug Bounty Report', 0, 1, 'C')
        pdf.set_font('Arial', '', 12)
        pdf.ln(10)
        pdf.cell(0, 10, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 0, 1, 'C')
        pdf.ln(10)

        # Add sections
        for section_title, section_body in scan_results.items():
            pdf.add_page()
            pdf.set_font('Arial', 'B', 12)
            pdf.cell(0, 10, section_title, 0, 1, 'L')
            pdf.set_font('Arial', '', 12)
            pdf.multi_cell(0, 10, section_body)

        # Save the PDF to file
        pdf.output(os.path.join(self.output_dir, report_filename))
        print(f"PDF report generated: {os.path.join(self.output_dir, report_filename)}")

    def generate_combined_report(self, scan_results):
        """Generate both HTML and PDF reports."""
        self.generate_html_report(scan_results)
        self.generate_pdf_report(scan_results)

# Sample scan results (you can replace this with dynamically generated results)
scan_results = {
    "Reconnaissance": "Subdomains discovered: \n- api.example.com \n- dev.example.com \n\nDNS records found: \n- A: 192.168.1.1 \n- CNAME: example.com.",
    "Vulnerability Scanning": "OWASP ZAP scan detected: \n- XSS vulnerability in /login \n- SQL Injection vulnerability in /search.",
    "Exploitation": "Exploit attempted on /admin: \n- Exploited Remote Code Execution vulnerability successfully.",
    "Findings & Recommendations": "The application is vulnerable to Cross-Site Scripting (XSS) and SQL Injection. It is recommended to implement input validation and output encoding."
}

if __name__ == "__main__":
    report_generator = ReportGenerator()
    report_generator.generate_combined_report(scan_results)
