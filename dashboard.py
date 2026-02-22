import tkinter as tk
from tkinter import ttk
from process_scanner import scan_processes
from startup_scanner import check_startup
from network_monitor import scan_connections
from risk_engine import calculate_risk
from report import generate_report


class SecurityDashboard:

    def __init__(self, root):

        self.root = root
        self.root.title("SentinelKeys Security Dashboard")
        self.root.geometry("800x520")
        self.root.resizable(False, False)

        title = tk.Label(
            root,
            text="SentinelKeys Cybersecurity Scanner",
            font=("Segoe UI", 18, "bold")
        )
        title.pack(pady=10)

        subtitle = tk.Label(
            root,
            text="Process • Startup • Network Monitoring",
            font=("Segoe UI", 10)
        )
        subtitle.pack()

        scan_btn = tk.Button(
            root,
            text="Run Security Scan",
            font=("Segoe UI", 11, "bold"),
            padx=15,
            pady=6,
            command=self.run_scan
        )
        scan_btn.pack(pady=15)

        columns = ("Type", "Detection")

        self.tree = ttk.Treeview(root, columns=columns, show="headings")

        self.tree.heading("Type", text="Type")
        self.tree.heading("Detection", text="Detection")

        self.tree.column("Type", width=120)
        self.tree.column("Detection", width=640)

        self.tree.pack(padx=20, pady=10, fill="both", expand=True)

        self.risk_label = tk.Label(
            root,
            text="Risk Score: 0   |   Threat Level: SAFE",
            font=("Segoe UI", 12, "bold")
        )
        self.risk_label.pack(pady=10)

    def run_scan(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        findings = []

        findings += scan_processes()
        findings += check_startup()
        findings += scan_connections()

        risk = calculate_risk(findings)

        if not findings:
            self.tree.insert("", "end", values=("info", "No suspicious activity found"))

        for item in findings:
            self.tree.insert(
                "",
                "end",
                values=(item["type"], item["message"])
            )

        self.risk_label.config(
            text=f"Risk Score: {risk['score']}   |   Threat Level: {risk['level']}"
        )

        if risk["level"] == "HIGH RISK":
            self.risk_label.config(fg="red")
        elif risk["level"] == "MEDIUM RISK":
            self.risk_label.config(fg="orange")
        else:
            self.risk_label.config(fg="green")

        generate_report(findings, risk)