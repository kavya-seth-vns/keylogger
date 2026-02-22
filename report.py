from datetime import datetime

def generate_report(findings , risk):

    filename = "security_report.txt"

    with open(filename, "w") as f:

        f.write("KEYLOGGER DETECTOR REPORT\n")
        f.write("="*40 + "\n\n")

        f.write(f"Scan Time: {datetime.now()}\n\n")

        for item in findings:
            f.write(f"[{item['type'].upper()}] {item['message']}\n")

        f.write("\n")

        f.write(f"Risk Score: {risk['score']}\n")
        f.write(f"Threat Level: {risk['level']}\n")


    print("\nReport saved as: ", filename)    