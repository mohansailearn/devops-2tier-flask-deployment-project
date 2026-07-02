from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)


def get_db():

    return mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="mydb"
    )


@app.route("/")
def home():

    return "2 Tier Flask Application Running 🚀"


@app.route("/message", methods=["POST"])
def message():

    data = request.json

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO messages(message) VALUES(%s)",
        (data["message"],)
    )

    conn.commit()

    return jsonify({"status":"saved"})


@app.route("/messages")
def get_messages():

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM messages")

    result = cursor.fetchall()

    return jsonify(result)


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
