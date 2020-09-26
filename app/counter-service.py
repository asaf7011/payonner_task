import flask
from flask import Flask,request
from multiprocessing import Value
from flask import Flask, jsonify


counter = Value('i', 0) #Define counter to 0
app = flask.Flask(__name__)


## Handle a GET request. returns counter value ##
@app.route('/', methods=['GET'])
def handle_get():
    out = counter.value
    return jsonify (NumberOfPostRequests=out) #Return counter value


## Handle a POST request increased counter by +1 and print "Received"- for your convenience ##
@app.route('/post', methods=['POST'])
def handle_post():
    with counter.get_lock():
        counter.value += 1
    return 'Received !' #Response to your request.
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="80") #Define host on port 80


