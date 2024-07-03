from netmiko import ConnectHandler

hosts = {
    'device_type' :'cisco_ios',
    'ip' :'192.168.122.212',
    'username' :'omar',
    'password' :'ali',
    'secret' :'ali',

}

netconnect = ConnectHandler(**hosts)
netconnect.enable()
output = netconnect.send_command('sh vl br')
output += netconnect.send_command('sh ip int br')

print(output)

config=['int loop 0','ip add 1.1.1.1 255.255.255.0','no shut']
output = netconnect.send_config_set(config)
output += netconnect.send_command('sh ip int br')

print(output)


for n in range(30,60):
    config=['vlan '+str(n),'name Vlan_'+str(n)]
    output=netconnect.send_config_set(config)
    print(output)
