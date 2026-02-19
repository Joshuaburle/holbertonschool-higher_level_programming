#!/usr/bin/python3
"""API Security & Authentication (Basic Auth + JWT + Roles)"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

# Strong secret key (for school projects it's fine hardcoded; in real life use env var)
app.config["JWT_SECRET_KEY"] = "change-this-secret-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory users (as specified)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


# --------------------------
# Basic Auth configuration
# --------------------------
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if not user:
        return None
    if check_password_hash(user["password"], password):
        return user
    return None


@auth.error_handler
def basic_auth_error(_status=None):
    # Must be 401 when credentials missing/invalid
    return jsonify({"error": "Unauthorized"}), 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# --------------------------
# JWT error handlers (MUST return 401 for auth errors)
# --------------------------
@jwt.unauthorized_loader
def handle_missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


# --------------------------
# JWT endpoints
# --------------------------
@app.route("/login", methods=["POST"])
def login():
    payload = request.get_json(silent=True)
    if payload is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = payload.get("username")
    password = payload.get("password")

    if not username or not password:
        # Keep it simple; not specified but reasonable
        return jsonify({"error": "Username and password required"}), 400

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        # Invalid credentials => 401
        return jsonify({"error": "Invalid credentials"}), 401

    # Embed role in identity payload (simple + explicit)
    identity = {"username": user["username"], "role": user["role"]}
    access_token = create_access_token(identity=identity)

    return jsonify({"access_token": access_token})


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    identity = get_jwt_identity()  # dict: {"username":..., "role":...}
    role = identity.get("role") if isinstance(identity, dict) else None

    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
