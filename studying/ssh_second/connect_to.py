import paramiko
import os
import logging
import time



class ConnectionToServer:
    def __init__(self, hostname, user, password, port=22):
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(hostname, port, user, password)
        except paramiko.ssh_exception.NoValidConnectionsError as ex:
            print("Some problem with connection has been detected: \n")
            print(ex)
            exit(555)

    def perform_tasks(self):
        """
        Method to perform task where you need to get output during some period of time
        :return
        """

        try:
            channel = self.ssh_client.invoke_shell()
            return channel
        except paramiko.SSHException as ex:
            print("Some problem during creating an invoke shell has been detected\n")
            print(ex)
            exit(555)

    def execute_command(self, command):
        """
        Execute 'one click' command. Example of execution 'execute_command("ls -la /fdsfsdf")'. It also
        handles stderr in case if it isn't empty
        :return:
        """
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        err = stderr.readlines()
        if err:
            for i in err:
                print(i)
                return ['Error has been detected during the execution of this command']
        else:
            return stdout.readlines()


class StdReader:
    def __init__(self, channel):
        self.channel = channel

    def stdout_handler(self, find='$ \''):
        """
        This method handles stdout from the command, before meets the command prompt.
        :return:
        """
        resp = ''
        while not str(resp).endswith(find):
            resp = self.channel.recv(9999)
            print(str(resp))


def is_it_alive(hostname, attempts=5, verbose=True):
    a = 0
    while a <= attempts:
        if os.system('ping -c 1 ' + hostname + ' 2>&1 > /dev/null') is 0:
            return True
        else:
            a += 1
            if verbose:
                print("Number of attempt to connect is " + str(a))
            if a == attempts:
                return False


def apps_logs(log_name='app_messages'):
    logger = logging.getLogger(log_name)
    logfile = "/opt/python/studying/ssh_second/{}.log".format(log_name)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(logfile)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger, logfile

