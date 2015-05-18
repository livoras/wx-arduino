from flask import Flask, request
from udp_arduino_server import wait_for_connection, server_sock, info
from threading import Thread

udp_thread = Thread(target=wait_for_connection)
udp_thread.start()

app = Flask(__name__)
old_msg = "good"

@app.route("/", methods=['GET', 'POST'])
def verify():
    global old_msg
    print request.method + "======================>>"
    if request.method == 'GET':
        old_msg = request.data
        return request.args.get('echostr', 'no')
    elif request.method == 'POST':
        old_msg = request.data
        print request.data, info['addr']
        server_sock.sendto(request.data, info['addr'])
        return "OK"

@app.route("/log")
def log():
    return old_msg

if __name__ == "__main__":
    app.run()
