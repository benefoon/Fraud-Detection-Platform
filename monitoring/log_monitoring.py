import re

def detect_anomalies(log_file):
    """Detect anomalies in security logs."""
    with open(log_file, 'r') as file:
        logs = file.readlines()
    suspicious_patterns = [r'failed login', r'unauthorized access']
    for pattern in suspicious_patterns:
        for log in logs:
            if re.search(pattern, log):
                print(f"Alert: {log}")
