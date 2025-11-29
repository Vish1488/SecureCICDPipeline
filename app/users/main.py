from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/users")
def users():
    return jsonify([
        {"id":"1", "name":"anakin"},
        {"id":"2", "name":"Vader"},
        {"id":"3", "name": "Padme"} 
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 8000)



