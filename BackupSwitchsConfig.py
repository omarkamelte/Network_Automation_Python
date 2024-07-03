import getpass
import telnetlib

print('     ')
print ('backingup switchs...')
print ('        ')

#getting credential from files
us = open('username')
user = us.readline()
user = user.strip()
pas=open('password')
password = pas.readline()
password = password.strip()

print('     ')
print ('Please seat back till finishing backup...')
print ('        ')

ips = open('MySwitchs')

for IP in ips:
    print('     ')
    print ('getting configuration from switch '+ IP)
    print ('        ')

    IP = IP.strip()
    tn = telnetlib.Telnet(IP)

    #Wait for username
    print('logging to switch')
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    print('logging to privilage mode')

    #access Enable mode
    tn.write(b"enable\n")
    #add enablemode pasword
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")


    #setting terminla to 0
    print('Collecting info') 
    tn.write(b"terminal length 0\n") 
    tn.write(b"show run\n") 
    tn.write(b"exit\n") 
    

    print('Saving info...')
    R = tn.read_all();
    print(R)
    sav = open('switch ' + IP, 'w')
    sav.write(R.decode('ascii'))
    sav.write('\n')
    sav.close

print('     ')
print ('Configuration is finished!')
print ('        ')
