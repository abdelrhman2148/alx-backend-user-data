import base64
from api.v1.auth.auth import Auth
from flask import request

class BasicAuth(Auth):
    """BasicAuth class for Basic Authentication."""

    def authorization_header(self, request=None):
        """Return the Authorization header."""
        if request is None:
            return None
        auth = request.headers.get('Authorization')
        if not auth:
            return None
        return auth

    def current_user(self, request=None):
        """Return the current user based on the Authorization header."""
        if request is None:
            return None
        auth_header = self.authorization_header(request)
        if not auth_header:
            return None

        # Extract username and password from the Authorization header
        try:
            parts = auth_header.split(" ")
            if len(parts) == 2 and parts[0] == "Basic":
                decoded = base64.b64decode(parts[1]).decode("utf-8")
                username, password = decoded.split(":")
                if username == "Test" and password == "Test":  # Example: you may change this
                    return username
        except Exception:
            return None
        return None
