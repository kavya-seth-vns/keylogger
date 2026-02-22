import psutil

def scan_connections():

    findings = []

    connections = psutil.net_connections(kind='inet')

    for conn in connections:

        if conn.raddr:

            ip = conn.raddr.ip
            port = conn.raddr.port

            findings.append({
                "type": "network",
                "message": f"Active connection to {ip}:{port}",
                "severity": 5,
            })

    return findings        