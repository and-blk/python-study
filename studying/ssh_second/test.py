"""

import os

HOST = '192.168.7.101'

if os.system('ping -c 1 ' + HOST + ' 2>&1 > /dev/null') == 0:
    print('successfully connected')
else:
    print("something is going wrong")


"""

import connect_to
import time

host = "192.168.7.101"
user = "user"
password = "user"
port = 22
responce = str()
state = False


if connect_to.is_it_alive(host, 2):
    print('it is alive')
    h = connect_to.ConnectionToServer(host, user, password, port)
    channel = h.perform_tasks()
    print("before perform")
    channel.send('sudo -S <<< "user" reboot \n')
    print("after perform")
    std_handler = connect_to.StdReader(channel)
    std_handler.stdout_handler('')
    time.sleep(10)
else:
    print("Host wasn't pinged successfully")
    exit(555)

while not state:
    state = connect_to.is_it_alive(host, 20, False)
print("waiting 10 sec")
time.sleep(10)
h = connect_to.ConnectionToServer(host, user, password, port)
if h:
    channel = h.perform_tasks()
    channel.send('sudo -S <<< "user" yum update -y \n')
    std_handler = connect_to.StdReader(channel)
    std_handler.stdout_handler()
else:
    print('problem with connection')


