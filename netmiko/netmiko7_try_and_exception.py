#!/usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
import time
from getpass import getpass
from netmiko import ConnectHandler
import colorama
from colorama import Fore, Back
import os
from hashlib import md5
from base64 import b64decode
from base64 import b64encode
import smtplib
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
from getpass import getpass
from netmiko import ConnectHandler
import sys

username = "cisco"
password = "cisco"


with open('devices_file.txt') as f:
    devices_list = f.read().splitlines()

for devices in devices_list:
    print ('Connecting to device" ' + devices)
    ip_address_of_device = devices
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': username,
        'password': password
    }
    try:
     net_connect = ConnectHandler(**ios_device)
    except (AuthenticationException):
     print('Authentication failure: ' + ip_address_of_device)
     continue
    except (NetMikoTimeoutException):
        print('Timeout to device: ' + ip_address_of_device)
        continue
    except (EOFError):
        print('End of file while attempting device ' + ip_address_of_device)
        continue
    except (SSHException):
        print('SSH Issue. Are you sure SSH is enabled? ' + ip_address_of_device)
        continue
    except Exception as unknown_error:
        print('Some other error: ' + str(unknown_error))
        continue
    output1 =net_connect.send_config_set("do sh ip int br")
    net_connect.save_config()
    net_connect.disconnect()
    print(output1)