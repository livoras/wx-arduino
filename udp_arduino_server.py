import socket
port = 6666
server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_sock.bind(("", port))
print "waiting on port:", port

info = {"addr": None}

def wait_for_connection():
    global info
    while True:
        data, addr = server_sock.recvfrom(1024)
        info["addr"] = addr
        print "New Connection:", info
        server_sock.sendto("OK", addr)

