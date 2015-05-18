from udp_arduino_server import wait_for_connection, server_sock, info
from threading import Thread

udp_thread = Thread(target=wait_for_connection)
udp_thread.start()

while True:
    cmd = raw_input()
    if cmd == 'exit': break
    print info

