import paramiko
from webapp import db
from webapp.models import Kernel


class DataProcessing:
    """
    This class is needed to get kernel version and append it
    to given list in data_collection method
    """

    """
    to reach remote host and execute uname -r
    """
    @staticmethod
    def remote_session(host, usr, pwd, ldata):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=host, username=usr, password=pwd)
            stdin, stdout, stderr =  client.exec_command('uname -r')
            output = str(stdout.read(), encoding='utf-8')
            ldata.append(output)
            return output
        except paramiko.AuthenticationException as auth_exception:
            ldata.append(auth_exception)
            return auth_exception
        except Exception as exc:
            ldata.append(exc)
            return exc
        finally:
            client.close()

    """
    Commit to db instance imported from init
    """
    @staticmethod
    def commit(host, vers):
        kernel = Kernel(server_name=host, version=vers)
        db.session.add(kernel)
        db.session.commit()

    @staticmethod ### method to read from db instance
    def fetch():
        return Kernel.query.all()











