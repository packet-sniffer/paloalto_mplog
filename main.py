#!usr/bin/python3
'''
This program is to extract contents from mp-log file and send an email when a condition is met
'''

# from netmiko import ConnectHandler
import paramiko
import os


username = os.environ['USER']
password = os.environ['PWD']


def connect_host(Host):
    host = Host
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(
        host,
        username=username,
        password=password
    )
    (
        ssh_stdin,
        ssh_stdout,
        ssh_stderr
    ) = ssh_client.exec_command(' ')
    ssh_stdin.channel.send("grep pattern 'failed to get group obj'  mp-log useridd.log")
    ssh_stdin.channel.shutdown_write()
    resp = ssh_stdout.read().decode('utf_8')
    ssh_client.close()
    return resp


def match_pattern(string1):
    if "failed to get group obj" in string1:
        return True
    else:
        return False


def send_email():
    pass
#plaeholder for email config


def main():
    out_string = connect_host('1.1.1.1')
    result1 = match_pattern(out_string)
    if result1 == True:
        print("error found")
        send_email()
    else:
        print("no error found")
        pass


if __name__ == '__main__':
    main()
