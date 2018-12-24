import paramiko


def param_ssh(hostname, user_name, password_sec, port_num, command):

    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname, port_num, user_name, password_sec)
        channel = ssh_client.invoke_shell()
    except paramiko.ssh_exception as ssh_excep:
        print("Seems there's a problem with ssh connection, take a look at the error: ")
        print(ssh_excep)

    return channel
