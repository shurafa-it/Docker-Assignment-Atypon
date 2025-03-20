from flask import Flask, jsonify
import mysql.connector
import pymongo
import os

app = Flask(__name__)

mysql_config = {
    "host": os.getenv("MYSQL_HOST", "mysql-db"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", "password"),
    "database": os.getenv("MYSQL_DATABASE", "data_db"),
}

mongo_client = pymongo.MongoClient("mongodb://mongo-db:27017/")
mongo_db = mongo_client["analytics_db"]
mongo_collection = mongo_db["results"]

@app.route("/analyze", methods=["GET"])
def analyze():
    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM records")
    values = [row[0] for row in cursor.fetchall()]
    conn.close()

    if values:
        results = {
            "max": max(values),
            "min": min(values),
            "avg": sum(values) / len(values),
        }
        results["_id"] = str(results.get("_id", ""))
        mongo_collection.insert_one(results)
        return jsonify(results)
    return jsonify({"message": "No data found"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

