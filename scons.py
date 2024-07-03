import getpass
import telnetlib

print('     ')
print ('Configuring the Switch...')
print ('        ')

# Configure the router
#HOST = ""
#user = input("Enter your Telnet account: ")
#password = getpass.getpass()
us = open('username')
user = us.readline()
pas=open('password')
password = pas.readline()

print('     ')
print ('Please seat back till finishing configuration...')
print ('        ')

ips = open('MySwitchs')

for IP in ips:
    print('     ')
    print ('configuring IP '+ IP)
    print ('        ')

    IP = IP.strip()
    tn = telnetlib.Telnet(IP)

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
    print(password.encode('ascii') + b"\n")


    #Create 10 vlans 
    tn.write(b"conf t\n")
    for x in range(2,4):
        tn.write(b"vlan " + str(x).encode() + b" \n")
        tn.write(b"name VL_"+ str(x).encode() + b"\n")
        print('     ')
        print ('vlan VL_' + str(x) + ' Is created')
        print ('        ')

    tn.write(b"end\n")
    print('end')
    tn.write(b"exit\n")
    print('exit')

    # print(tn.read_all().decode('ascii'))

print('     ')
print ('Configuration is finished!')
print ('        ')
