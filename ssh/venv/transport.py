import paramiko
import time

host = "192.168.7.77"
user = "root"
password = "root"
port = 22
command = 'apt-get remove tcpdump'


def ssh_con(hostname, user_name, password_sec, port_num, command):
    stream_data = str()
    resp = str()
    ssh_client = paramiko.SSHClient()

    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname, port_num, user_name, password_sec)
    channel = ssh_client.invoke_shell()
    time.sleep(2)
    channel.send(command)
    channel.send('\n')
    while not stream_data.find('[Y/n]'):
        resp = channel.recv(9999)
        stream_data += str(resp)
        print(resp)
        if resp.find('is not installed') != -1:
            print("can't be inplemented: " + command)
            break
    else:
        channel.send('Y\n')
        print("was broken")
    print('end loop')

    stream_data2 = str()
    while not stream_data2.endswith('root@ubuntu_pyt:~# \''):
        resp2 = channel.recv(9999)
        stream_data2 += str(resp2)
        print(resp2)

    print("successfully done")

ssh_con(host, user, password, port, command)
