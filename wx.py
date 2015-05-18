from flask import Flask, request
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
        print request.data
        return "OK"

@app.route("/log")
def log():
    return old_msg

if __name__ == "__main__":
    app.run()
