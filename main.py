import psutil
import platform
import rich
import paramiko

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

remote_file.close()
sftp.close()
ssh.close()