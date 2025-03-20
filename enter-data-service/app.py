from flask import Flask, request, jsonify
import requests
import mysql.connector
import os

app = Flask(__name__)

AUTH_SERVICE_URL = "http://authentication-service:5001/auth"

db_config = {
    "host": os.getenv("MYSQL_HOST", "mysql-db"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", "password"),
    "database": os.getenv("MYSQL_DATABASE", "data_db"),
}

@app.route("/enter", methods=["POST"])
def enter_data():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    value = data.get("value")

    auth_response = requests.post(AUTH_SERVICE_URL, json={"username": username, "password": password})
    if auth_response.status_code != 200:
        return jsonify({"message": "Authentication failed"}), 401

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO records (value) VALUES (%s)", (value,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Data entered successfully"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
