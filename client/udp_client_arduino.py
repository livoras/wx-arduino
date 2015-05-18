import re
import socket
import time
from threading import Thread
from arduino import controll
    
SERVER_UDP_IP = "138.128.210.114"
SERVER_UDP_PORT = 6666

print "UDP target IP:", SERVER_UDP_IP
print "UDP target port:", SERVER_UDP_PORT

client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def connect():
    client_sock.sendto("connect", (SERVER_UDP_IP, SERVER_UDP_PORT))

def recv():
    while True:
        data = client_sock.recvfrom(20480)
        controll(parse_content(data[0]))

def heartbeat():
    while True:
        print "heartbeat!"
        connect()
        time.sleep(30)

def parse_content(data):
    result = re.search("(?<=\<Content\>\<!\[CDATA\[)[\S\s]*(?=\]\]\>\<\/Content\>)", data)
    if result:
        return result.group()
    else:
        return data

if __name__ == "__main__":
    heartbeat_thread = Thread(target=heartbeat)
    heartbeat_thread.daemon = True
    heartbeat_thread.start()
    recv()
