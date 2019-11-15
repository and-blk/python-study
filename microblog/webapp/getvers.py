import paramiko


class GetVersion:
    """
    This class is needed to get kernel version and append it
    to given list in data_collection method
    """

    @staticmethod
    def remote_session(host, usr, pwd):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=host, username=usr, password=pwd)
            stdin, stdout, stderr =  client.exec_command('uname -r')
            output = str(stdout.read(), encoding='utf-8')
            return output
        except paramiko.AuthenticationException:
            return 'auth exception'
        except:
            return 'can\'t connect'
        finally:
            client.close()

    @staticmethod
    def data_collection(hosts, usr, pwd, list_data):
        for host in hosts:
            list_data.append(GetVersion.remote_session(host, usr, pwd))





