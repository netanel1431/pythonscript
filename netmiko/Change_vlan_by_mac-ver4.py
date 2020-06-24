
# !/usr/bin/env python
import time
from getpass import getpass
from netmiko import ConnectHandler
from netaddr import EUI
import netaddr

print("-----Hello this script work only on cisco device that support ssh ver 2------")
username = input('Enter your SSH username: ')
password = getpass()
ip_address_of_device = input('Enter the ip address of the device,like: 192.168.1.1: ')
print("")
Department1="BusinessDevelopment -   172.20.1.0/24-  VLAN 201"
Department2="Currency -              172.20.2.0/24-  VLAN 202"
Department3="CyberSecurity -         172.20.3.0/24-  VLAN 203"
Department4="Financial -             172.20.4.0/24-  VLAN 204"
Department5="General Management -    172.20.5.0/24-  VLAN 205"
Department6="Human Resources -       172.20.6.0/24-  VLAN 206"
Department7="Information Technology- 172.20.7.0/24-  VLAN 207"
Department8="InternalAuditor -       172.20.8.0/24-  VLAN 208"
Department9="Legal -                 172.20.9.0/24-  VLAN 209"
Department10="Logistics -            172.20.10.0/24- VLAN 210"
Department11="ProjectManagement -    172.20.11.0/24- VLAN 211"
Department12="RealEstate -           172.20.12.0/24- VLAN 212"
Department13="BackOffice -           172.20.13.0/24- VLAN 213"
Department14="Retail -               172.20.14.0/24- VLAN 214"
Department15="Risk Assessment -      172.20.15.0/24- VLAN 215"
print(Department1)
print(Department2)
print(Department3)
print(Department4)
print(Department5)
print(Department6)
print(Department7)
print(Department8)
print(Department9)
print(Department10)
print(Department11)
print(Department12)
print(Department13)
print(Department14)
print(Department15)
print(" ")
vlan = input("Enter the VLAN number of the Department: 201,202,203,204,205,206,207,208,209,210,211,212,213,214,215: ")
print ("")
print ("The VLAN  is:", vlan)
print (" ")
a=0
while (a==0):
 if vlan == "201":
    desc_vlan ="BusinessDevelopment"
    a=1
 elif vlan == "202":
    desc_vlan ="Currency"
    a=1
 elif vlan == "203":
    desc_vlan ="CyberSecurity"
    a=1
 elif vlan == "204":
    desc_vlan ="Financial"
    a=1
 elif vlan == "205":
    desc_vlan ="General Management"
    a=1
 elif vlan == "206":
    desc_vlan ="Human Resources"
    a=1
 elif vlan == "207":
    desc_vlan ="Information Technology"
    a=1
 elif vlan == "208":
    desc_vlan ="InternalAuditor"
    a=1
 elif vlan == "209":
    desc_vlan ="Legal"
    a=1
 elif vlan == "210":
    desc_vlan ="Logistics"
    a=1
 elif vlan == "211":
    desc_vlan ="ProjectManagement"
    a=1
 elif vlan == "212":
    desc_vlan ="RealEstate"
    a=1
 elif vlan == "213":
    desc_vlan ="BackOffice"
    a=1
 elif vlan == "214":
    desc_vlan ="Retail"
    a=1
 elif vlan == "215":
    desc_vlan ="Risk Assessment"
    a=1
 else:
    print("error- Invalid VLAN number")
    a=0
    vlan = input("Enter the VLAN number of the Department: 200,201,202,203,204,205,206,207,208,209,210,211,212,213,214:")
    print(" ")
    print("The VLAN  is:", vlan)
    print(" ")
#port=input("ENTER the port number of the switch' like: gi1/0/1 ,gi2/0/1 , gi1/1/1: ")
#print (" the port is:", port)

mac1 =input("Enter the MAC address of the pc-card on format of:f8ca.b84a.122d or F8-CA-B8-4A-12-2D ,now enter the MAC:")
mac = str(mac1)
if "-" in mac:
 abc = EUI(mac)
 abc.dialect = netaddr.mac_cisco
 new_mac = str(abc)
elif "." in mac:
    new_mac = mac.lower()
else:
    new_mac = list(mac)
    new_mac = mac[0] + mac[1] + mac[2] + mac[3] + "." + mac[4] + mac[5] + mac[6] + mac[7] + "." + mac[8] + mac[9] + mac[10] + mac[11]
    new_mac=new_mac.lower()


print(" ")

print('Connecting to device: ' + ip_address_of_device)
print(" ")

ios_device = {
    'device_type': 'cisco_ios',
    'ip': ip_address_of_device,
    'username': username,
    'password': password
}
net_connect = ConnectHandler(**ios_device)
config_commands = [
        'do sh MAC address-table dynamic address '+new_mac
		]

output = net_connect.send_config_set(config_commands)

config_commands1 = [
        'do sh int trunk'
		]
output1 = net_connect.send_config_set(config_commands1)

finish = net_connect.save_config()
net_connect.disconnect()

lines = output.splitlines()
for i in lines:
    split1 = i.split()
    if new_mac in split1:

         for f in split1:
           if "Gi" or "Fa" in f:
            port = f

print('The MAC address {} is connected to port "{}"'.format(new_mac,port))
print(" ")


error= True

lines1 = output1.splitlines()
for i in lines1:
    split1 = i.split()
    if port in split1:
         for f in split1:
           if "Trunk" or "trunk" or "trunking" in f:
            error =False


##########################################################################################
##########################################################################################
time.sleep(1)
if error ==  True:
 ios_device = {
    'device_type': 'cisco_ios',
    'ip': ip_address_of_device,
    'username': username,
    'password': password
         }
 net_connect = ConnectHandler(**ios_device)


 config_commands = [
        'vlan' " "+ vlan,
		'name' " "+ desc_vlan,
		'Interface ' + port,
		'switchport access vlan '+ vlan, #User enters VLAN number
        'sh',
        'no sh',
        "do show run int "+port
		]

 output = net_connect.send_config_set(config_commands)

 net_connect.save_config()
 net_connect.disconnect()

 print (output)
else:print("Error-The port: {} is a Trunk port, You only can config access port".format(port))

print(" ")
input("Press Any Key To Finish")


