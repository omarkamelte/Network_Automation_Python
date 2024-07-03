from TelNetSwitchs import TelNetSwitchs

ts = TelNetSwitchs()
user = ts.GetUser('username')

password = ts.fitchpass('password')
ips = open('MySwitchs')
for i in ips:
 
    tn=ts.TelnetConn(i,user,password)

    print('\n\n Deleting Vlans..\n\n')
    ts.AddVlans(tn,2,50)
    print(tn.read_all().decode('ascii'))
    
    print('\n\nSwitch '+i + 'is Configured\n\n')
#    time.sleep(3)
print ('****************')
print('\n\nconnection done\n\n')
print ('****************')