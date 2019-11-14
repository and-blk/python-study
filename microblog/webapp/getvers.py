import paramiko


class GetVersion:
    host = 'localhost'
    usr = 'user'
    pwd = 'user'

    @classmethod
    def remote_cmd(cls):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=cls.host, username=cls.usr, password=cls.pwd)
            stdin, stdout, stderr =  client.exec_command('uname -r')
            output = str(stdout.read(), encoding='utf-8')
            return output
        except:
            print('auth exc')
        finally:
            client.close()


