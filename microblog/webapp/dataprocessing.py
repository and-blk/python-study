import paramiko
import sys


class DataProcessing:
    """
    This class is needed to get kernel version and append it
    to given list in data_collection method
    """

    """
    to reach remote host and execute uname -r
    """
    @staticmethod
    def remote_session(host, usr, pwd, list_data):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=host, username=usr, password=pwd)
            stdin, stdout, stderr =  client.exec_command('uname -r')
            output = str(stdout.read(), encoding='utf-8')
            list_data.append(output)
        except paramiko.AuthenticationException as auth_exception:
            list_data.append(auth_exception)
        except Exception as exc:
            list_data.append(exc)
        finally:
            client.close()








