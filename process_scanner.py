import psutil

SUSPICIOUS_KEYWORDS = ['keylogger', 'logger', 'hook' , 'keyboard' , 'capture' , 'spyware', 'malware', 'hacker', 'stealer']

def scan_processes():

    findings = []

    for proc in psutil.process_iter(['pid', 'name' , 'exe']):

        try:
            name = proc.info['name'].lower()

            for word in SUSPICIOUS_KEYWORDS:
                if word in name:
                    findings.append({
                        "type": "process",
                        "message": f"Suspicious process name: {name}",
                        "severity": 40,
                    })

        except:
            pass

    return findings                