import getpass
import telnetlib

HOST = "192.168.185.130"

user = input("Enter your Telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# Modo enable
tn.write(b"enable\n")
tn.write(b"cisco\n")

# Configuración
tn.write(b"configure terminal\n")

# Loopback0
tn.write(b"interface loopback 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
tn.write(b"exit\n")

# Loopback1
tn.write(b"interface loopback 1\n")
tn.write(b"ip address 2.2.2.2 255.255.255.255\n")
tn.write(b"exit\n")

# OSPF
tn.write(b"router ospf 1\n")
tn.write(b"network 2.2.2.2 0.0.0.0 area 0\n")
tn.write(b"exit\n")

# Guardar configuración
tn.write(b"end\n")
tn.write(b"write memory\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))