from TelNetSwitchs import TelNetSwitchs
import threading

ts = TelNetSwitchs()
password = ts.fitchpass('password')
user = ts.GetUser('username')

def SwitchThread(i,user,password):
    tn=ts.TelnetConn(i,user,password)
    print('\n\n Deleting Vlans..\n\n')
    ts.removeVlans(tn,2,50)
    print(tn.read_all().decode('ascii'))

ips = open('MySwitchs')
for i in ips:
    x = threading.Thread(target=SwitchThread, args=(i,user,password,))
    x.start()
    
    
    print('\n\nSwitch '+i + 'is Configured\n\n')
#    time.sleep(3)
print ('****************')
print('\n\nconnection done\n\n')
print ('****************')