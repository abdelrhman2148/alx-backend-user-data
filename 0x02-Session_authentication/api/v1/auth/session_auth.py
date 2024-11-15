from flask import request, jsonify
from models.user import User
from api.v1.views import app_views
from api.v1.app import auth  # Import auth here to avoid circular imports
from werkzeug.exceptions import BadRequest

@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Handles login for session authentication"""
    # Retrieve email and password from the form data
    email = request.form.get('email')
    password = request.form.get('password')

    # Check if email is missing
    if not email:
        return jsonify({"error": "email missing"}), 400

    # Check if password is missing
    if not password:
        return jsonify({"error": "password missing"}), 400

    # Retrieve the user by email
    user = User.search({'email': email})

    # If no user is found, return an error
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    user = user[0]

    # Check if the password is valid
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Create a session ID for the user
    session_id = auth.create_session(user.id)

    # Get the dictionary representation of the user
    user_dict = user.to_json()

    # Set the session cookie
    response = jsonify(user_dict)
    session_name = getenv('SESSION_NAME')  # Get session name from environment
    response.set_cookie(session_name, session_id)

    return response
