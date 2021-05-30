from flask import Flask, jsonify, request
import time

app = Flask(__name__)
@app.route("/bot", method=["POST"])


# response 
def response():
    query = dict(request.from)['query']
    result = query +" "+ time.ctime()
    return jsonify({"response" : result})

if __name__ == "__main__":
    app.return(host="0.0.0.0",)