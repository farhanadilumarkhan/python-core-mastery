import re

def run_security_audit(file_path):
    print("Enterprise Security Audit Report")

    try:
        with open(file_path, 'r') as file:
            log_data = file.read()
            print(f"Successfully read log file: {file_path}")

            ip_pattern = r"\d{3}\.\d{1,3}\.\d{1,3}\.\d{1,2}"
            email_pattern = r"[a-zA-Z0-9\._]+@[a-z-]+\.[a-z]{2,3}"
            txn_pattern = r"\d{5}-[A-Z]{3}"
            alert_pattern = r".*(?:CRITICAL_ERROR|SECURITY_ALERT).*"

            extracted_ips = re.findall(ip_pattern, log_data)
            extracted_emails = re.findall(email_pattern, log_data)
            extracted_txns = re.findall(txn_pattern, log_data)
            extracted_alerts = re.findall(alert_pattern, log_data)

            print("Extracted IP Addresses:")
            for ip in extracted_ips:
                print(f"-> {ip}")

            print("Extracted Emails:")
            for email in extracted_emails:
                print(f"-> {email}")

            print("System Transaction Tracked:")
            for txn in extracted_txns:
                print(f"-> TXN_ID: {txn}")

            print("Critical Threads Alerts")
            for alert in extracted_alerts:
                print(f"-> {alert.strip()}")

        
    except FileNotFoundError:
        print(f"Error: '{file_path}' does not exist, please check your log file")
    except Exception as e:
        print(f"Error: {e}")

log_file_path = "server.log"
run_security_audit(log_file_path)