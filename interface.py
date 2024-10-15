import tkinter as tk
from tkinter import messagebox
from reconnaissance.recon import subdomain_enumeration
from scanners.scanner import zap_scan
from reporting.report_generator import generate_report

def start_scan():
    target = target_entry.get()
    if not target:
        messagebox.showwarning("Input Error", "Please enter a target URL.")
        return
    log_text.insert(tk.END, f"Starting scan for {target}...\n")
    subdomains = subdomain_enumeration(target)
    scan_results = zap_scan(target)
    log_text.insert(tk.END, f"Scan complete for {target}. Found {len(scan_results)} issues.\n")
    generate_report(scan_results)

def generate_report_callback():
    target = target_entry.get()
    scan_results = zap_scan(target)
    generate_report(scan_results)
    messagebox.showinfo("Report", "Vulnerability report generated successfully.")

root = tk.Tk()
root.title("Bounty Hunter - Automated Bug Bounty Tool")

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Target URL:").grid(row=0, column=0, padx=5)
target_entry = tk.Entry(input_frame, width=50)
target_entry.grid(row=0, column=1, padx=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

scan_button = tk.Button(button_frame, text="Start Scan", command=start_scan)
scan_button.grid(row=0, column=0, padx=10)

report_button = tk.Button(button_frame, text="Generate Report", command=generate_report_callback)
report_button.grid(row=0, column=1, padx=10)

log_frame = tk.Frame(root)
log_frame.pack(pady=10)

log_text = tk.Text(log_frame, width=80, height=20)
log_text.pack()

footer = tk.Label(root, text="Made by Davycipher", font=("Helvetica", 10), fg="grey")
footer.pack(side=tk.BOTTOM)

root.mainloop()
