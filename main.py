from process_scanner import scan_processes
from startup_scanner import check_startup
from network_monitor import scan_connections
from risk_engine import calculate_risk
from report import generate_report


def main():

    print("\n==============================")
    print(" SentinelKeys Security Scanner")
    print("==============================\n")

    findings = []

    try:
        print("[+] Scanning running processes...")
        findings += scan_processes()
    except Exception as e:
        print("Process scan error:", e)

    try:
        print("[+] Checking startup items...")
        findings += check_startup()
    except Exception as e:
        print("Startup scan error:", e)

    try:
        print("[+] Monitoring network connections...")
        findings += scan_connections()
    except Exception as e:
        print("Network scan error:", e)

    risk = calculate_risk(findings)

    print("\nScan Complete")
    print("Risk Score:", risk["score"])
    print("Threat Level:", risk["level"])

    generate_report(findings, risk)


if __name__ == "__main__":
    main()