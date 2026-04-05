def map_anomaly_to_mitre(cpu, network, login_attempts, process_count):

    threats = []

    if cpu > 80:
        threats.append({
            "technique": "Resource Hijacking",
            "mitre_id": "T1496",
            "reason": "High CPU usage may indicate cryptomining malware."
        })

    if network > 50:
        threats.append({
            "technique": "Data Exfiltration",
            "mitre_id": "T1041",
            "reason": "Large outbound traffic may indicate data exfiltration."
        })

    if login_attempts > 10:
        threats.append({
            "technique": "Brute Force",
            "mitre_id": "T1110",
            "reason": "High login attempts indicate brute force attacks."
        })

    if process_count > 120:
        threats.append({
            "technique": "Malware Execution",
            "mitre_id": "T1059",
            "reason": "High process count may indicate malicious scripts."
        })

    return threats