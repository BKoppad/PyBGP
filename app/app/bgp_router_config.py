from paramiko import SSHClient, AutoAddPolicy
import time

def connect_ssh(router):
    '''Connecting to router and returning sshClient object'''
    ssh_client = SSHClient()
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())
    print(f'Connecting to {router["hostname"]}')
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
    return ssh_client

def cli_access(ssh_client):
    '''Executing commands on supplied sshClient object or resepctive router'''
    shell = ssh_client.invoke_shell()
    print(shell.send_ready())
    shell.send('enable\n')
    shell.send('cisco\n')
    time.sleep(1)
    output = shell.recv(10000).decode()
    print(output)
    command = " "
    
    while command != 'exit':
        command= input("i/p > ")
        shell.send(f"{command}\n")
        time.sleep(3)
        output=shell.recv(10000).decode()
        print(output)


# creating a dictionary for each device to connect to
router1 = {'hostname': '10.1.1.10', 'port': '22', 'username':'bkoppad', 'password':'cisco'}
router2 = {'hostname': '10.1.1.20', 'port': '22', 'username':'bkoppad', 'password':'cisco'}

routers = [router1,router2]

for router in routers:
    ssh_client = connect_ssh(router)
    cli_access(ssh_client)

    if ssh_client.get_transport().is_active() == True:
        print('Closing connection')
        ssh_client.close()