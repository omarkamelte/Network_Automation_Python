import getpass
import telnetlib

print('     ')
print ('Configuring the Switch...')
print ('        ')

# Configure the router
HOST = "192.168.122.224"
user = input("Enter your Telnet account: ")
password = getpass.getpass()

print('     ')
print ('Please seat back till finishing configuration...')
print ('        ')


tn = telnetlib.Telnet(HOST)

#Wait for username
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

#access Enable mode
tn.write(b"enable\n")
#add enablemode pasword
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")

#show new state
#tn.write(b"sh ip int bri\n")


#Create 10 vlans 
tn.write(b"conf t\n")
for x in range(2,10):
    tn.write(b"vlan " + str(x).encode() + b" \n")
    tn.write(b"name VL_"+ str(x).encode() + b"\n")
    print('     ')
    print ('vlan VL_' + str(x) + ' Is created')
    print ('        ')

tn.write(b"end\n")

#show new state
#tn.write(b"sh ip int bri\n")


tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
