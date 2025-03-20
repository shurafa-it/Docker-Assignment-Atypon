from flask import Flask, request, jsonify

app = Flask(__name__)

users = {"admin": "password"}

@app.route("/auth", methods=["POST"])
def authenticate():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if users.get(username) == password:
        return jsonify({"message": "Authenticated"}), 200
    return jsonify({"message": "Authentication failed"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
