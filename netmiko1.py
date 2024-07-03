from netmiko import ConnectHandler


connections={'device_type': 'cisco_ios',
'ip': '192.168.122.224',
'username': 'omar',
'password': 'ali'
,'secret':'ali'}

net_connect = ConnectHandler(**connections)
net_connect.enable()
output =net_connect.send_command('show ip int brief')
print(output)
config_commands = [ 'int loop 0', 'ip addre 1.1.1.1 255.255.255.0', 'no sh']
output = net_connect.send_config_set(config_commands)
print (output)
output =net_connect.send_command('show ip int brief')
print (output)

for n in range(2,21):
    print ('Creat VLAN'+str(n))
    config_commands = ['vlan '+str(n),'name Python_Vlan'+str(n)]
    output = net_connect.send_config_set(config_commands)
    print(output)