import psutil
import platform
import rich
import paramiko
import json

host = "192.168.0.33"
username = "root"
key_file = "C:\\Users\\ronve\\.ssh\\id_rsa"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=username, key_filename=key_file)

sftp = ssh.open_sftp()
remote_file = sftp.file("/var/log/nginx/access.log", "r")
for line in remote_file:
    rich.print(line)

log_report = {"Errors": [], "Warnings": []}
for line in remote_file:
    if "error" in line.lower():
        log_report["Errors"].append(line)
    elif "warning" in line.lower():
        log_report["Warnings"].append(line)

remote_file.close()
sftp.close()
ssh.close()

#wegschrijven naar JSON bestand
with open("log_report.json", "w") as json_file:
    json.dump(log_report, json_file)

    rich.print(f"Log report saved to log_report.json")