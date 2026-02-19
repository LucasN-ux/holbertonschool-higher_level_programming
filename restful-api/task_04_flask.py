#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users= {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route("/")
def home():
    return "<p>Welcome to the Flask API!</p>"

@app.route("/data")
def get_usernames():
    usernames= list(users.keys())
    return jsonify(usernames)

@app.route("/users/<username>")
def get_user(username):
    user_info = users.get(username)
    
    if user_info:
        return jsonify(user_info)
    else:
        return jsonify({"error": "User not found"})

@app.route("/add_user", methods=["POST"])
def add_user():
    if not request.is_json:
        return jsonify({"error":"Invalid JSON"}), 400

    data = request.get_json

    username = data.get("username")

    if not username:
        return jsonify({"error":"Username is required"}), 400

    if username in users:
        return jsonify({"error":"Username already exists"}), 409

    users[username] = data

    return jsonify({
        "message": "User added successfully",
        "user": users[username]
    }), 201

@app.route("/status")
def get_status():
    return ("OK")

if __name__ == "__main__": app.run()
