import getpass
import time
import telnetlib

print('connecting...')

# user = input('Please add your username:')
# user = user.strip().encode('ascii') +b'\n'
# password= getpass.getpass();
# password = password.strip().encode('ascii') +b'\n'

us = open('username')
user = us.readline()
user = user.strip().encode('ascii') +b'\n'
pas=open('password')
password = pas.readline()
password = password.strip().encode('ascii') +b'\n'

ips = open('MySwitchs')
for i in ips:
    print('connecting '+i)
    tn = telnetlib.Telnet(i.strip())
    tn.read_until(b'Username: ')
    tn.write(user)
    tn.read_until(b"Password: ")
    tn.write(password)

    print('getting into privilage mode')
    tn.write(b'enable\n')
    tn.read_until(b"Password: ")
    tn.write(password)
    print('\n\nopening Config\n\n')
    tn.write(b'conf t\n')

    #print(tn.read_all().decode('ascii'))

    print('\n\n creating Vlans..\n\n')
    for x in range(2,50):
        v = 'no vlan ' + str(x)+ '\n'
        v=v.encode('ascii')
        tn.write(v)
        
        print('Vlan Deleted Vlan_'+str(x))
#        time.sleep(0.1)
    tn.write(b'end\n')
    tn.write(b'exit\n')
    print(tn.read_all().decode('ascii'))
    
    print('\n\nSwitch '+i + 'is Configured\n\n')
#    time.sleep(3)
print ('****************')
print('\n\nconnection done\n\n')
print ('****************')








