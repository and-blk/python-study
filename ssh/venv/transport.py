import paramiko
import time
import ssh_con

host = "192.168.7.101"
user = "user"
password = "user"
port = 22
command = input("Put your command here: ")
full_cmd = "sudo -S <<< '%s' %s \n" % (password, command)

resp = str()
resp2 = str()
resp0 = str()


channel = ssh_con.param_ssh(host, user, password, port, full_cmd)

while not str(resp0).endswith('$ \''):
    resp0 = channel.recv(9999)
    print(str(resp0))
print("==================================================================================================")
print('***********************' + full_cmd + '******************************')
print("==================================================================================================")
channel.send(full_cmd)

#while not str(resp).endswith('[y/N]: \''):
#    resp = channel.recv(9999)
#    print(resp)
#print("say yes")

while not str(resp2).endswith('$ \''):
    resp2 = channel.recv(9999)
    print(resp2)

print("==================================================================================================")
print('***********************' + 'successfully done' + '******************************')
print("==================================================================================================")