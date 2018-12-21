import paramiko
import time
import json

host = "192.168.7.77"
user = "root"
password = "root"
port = 22
data = {}
data_up = {}

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, user, password)

stdin, stdout, stderr = ssh.exec_command('apt-get update')

data_up['host3'] = stdout.readlines()

with open('/opt/python/ssh/venv/json_data.json', 'r') as f:
    data = json.load(f)
    data.update(data_up)

with open('/opt/python/ssh/venv/json_data.json', 'w') as fjs:
    json.dump(data, fjs)

#file = open('/opt/python/ssh/venv/json_data.json', 'a')
#json.dump(data, file)
#file.close()

#file_open = open('/opt/python/ssh/venv/json_data.json', 'r')
#data_open = json.load(file_open)
#print(data_open)
#file_open.close()
#ssh.close()