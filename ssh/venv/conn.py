import paramiko
import time

host = "192.168.7.77"
user = "root"
password = "root"
port = 22
command = 'apt-get upgrade'

def ssh_con(hostname, user_name, password_sec, port_num, command):
    ssh_client = paramiko.SSHClient()

    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname, port_num, user_name, password_sec)
    stdin, stdout, stderr = ssh_client.exec_command(command)
    ssh_client.send('y\n')
    print(stdout.readlines())


if __name__=='__main__':
    ssh_con(host, user, password, port, command)
