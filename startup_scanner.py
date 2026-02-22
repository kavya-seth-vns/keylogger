import os

def check_startup():

    findings = []

    startup_path = os.path.expandvars(
        r"%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
    )

    if not os.path.exists(startup_path):
        return findings

    try:
        files = os.listdir(startup_path)

        suspicious = [
            "keylogger","logger","hook","keyboard",
            "capture","spyware","malware","stealer"
        ]

        for f in files:

            name = f.lower()

            if any(word in name for word in suspicious):
                findings.append({
                    "type": "startup",
                    "message": f"Suspicious startup item: {f}",
                    "severity": 30
                })

    except Exception as e:
        print("Startup scan error:", e)

    return findings