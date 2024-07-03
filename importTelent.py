import getpass
import telnetlib

HOST = "192.168.122.222"
user = input("Enter your Telnet account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
#add enablemode pasword
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")
tn.write(b"int loopback 0\n")
tn.write(b"ip add 1.1.1.1 255.255.255.255\n")
tn.write(b"no shut\n")
tn.write(b"end\n")

tn.write(b"sh ip int bri\n")


tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))