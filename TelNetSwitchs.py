import getpass
import time
import telnetlib
class TelNetSwitchs:
    

    def __init__(self):
        self = self
    
    def GetUser(self,us):
        users = open('username')
        user = users.readline()
        user = user.strip().encode('ascii') +b'\n'
        return user

    def fitchpass(self,passs):
        passs=open('password')
        password = passs.readline()
        password = password.strip().encode('ascii') +b'\n'
        return password

    def TelnetConn(self,host,user,password):
        print('connecting '+host)
        tn = telnetlib.Telnet(host.strip())
        print(host)
        print(user)
        print(password)
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
        return tn
    def removeVlans(tn,frm,to):
        for x in range(frm,to):
            v = 'no vlan ' + str(x)+ '\n'
            v=v.encode('ascii')
            tn.write(v)
            
            print('Vlan Deleted Vlan_'+str(x))
            time.sleep(0.1)
        tn.write(b'end\n')
        tn.write(b'exit\n')

    def AddVlans(self,tn,frm,to):
        for x in range(frm,to):
            v = 'vlan ' + str(x)+ '\n'
            v=v.encode('ascii')
            tn.write(v)
            
            print('Vlan Created Vlan_'+str(x))
            time.sleep(0.1)
        tn.write(b'end\n')
        tn.write(b'exit\n')