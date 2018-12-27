import connect_to
import time
import getpass

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
    ex_text = "Host is in down state or there is a problem with connection"
    logger, logfile = connect_to.apps_logs()
    logger.warning(getpass.getuser() + " - " + ex_text)
    print("Wasn't successfully, take a look at " + logfile)
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


