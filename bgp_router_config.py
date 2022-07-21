import paramiko
import time
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# creating a dictionary for each device to connect to
router1 = {'hostname': '10.1.1.10', 'port': '22', 'username':'bkoppad', 'password':'cisco'}
router2 = {'hostname': '10.1.1.20', 'port': '22', 'username':'bkoppad', 'password':'cisco'}
router1_cfg = {'interface':'gi0/1'}
router2_cfg = {'interface':'gi0/1'}

# creating a list of dictionaries (of devices)
routers = [router1,router2]

# iterating over the list (over the devices) and backup the config
for router in routers:
    print(f'Connecting to {router["hostname"]}')
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
    shell = ssh_client.invoke_shell()

    shell.send('enable\n')
    shell.send('cisco\n')
    shell.send('conf t\n')
    print("Adding Router Interface for Router", router)

    if router["hostname"]=='10.1.1.10':
        shell.send('int gi0/1\n')
        shell.send('ip address 10.1.11.1 255.255.255.0\n')
        shell.send('int lo0\n')
        shell.send('ip address 1.1.1.1 255.255.255.0\n')
        shell.send('no shutdown\n')
        shell.send('router bgp 100\n')
        shell.send('neighbor 10.1.22.2 remote-as 100\n')
    elif router["hostname"]=='10.1.1.20': 
        shell.send('int gi0/1\n')
        shell.send('ip address 10.1.22.2 255.255.255.0\n')
        shell.send('int lo0\n')
        shell.send('ip address 2.2.2.2 255.255.255.0\n')
        shell.send('no shutdown\n')
        shell.send('router bgp 200\n')
        shell.send('neighbor 10.1.11.1 remote-as 100\n')

    shell.send('end\n')
    shell.send('terminal length 0\n')
    shell.send('show ip interface brief\n')
    shell.send('show ip bgp summary')
    time.sleep(10)

    output = shell.recv(1000000).decode()
    print(output)


if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()