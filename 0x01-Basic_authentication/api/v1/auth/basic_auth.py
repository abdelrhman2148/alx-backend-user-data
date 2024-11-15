from api.v1.auth.auth import Auth
import base64

class BasicAuth(Auth):
    """BasicAuth class for Basic Authentication."""

    def authorization_header(self, request=None) -> str:
        """Retrieve the Authorization header and validate it."""
        if request is None:
            return None
        auth_header = request.headers.get('Authorization')
        if auth_header is None or not auth_header.startswith("Basic "):
            return None
        return auth_header

    def current_user(self, request=None):
        """Retrieve the current user from the request."""
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None
        # Extract the base64-encoded credentials after "Basic "
        base64_credentials = auth_header.split(" ")[1]
        
        # Decode the credentials (username:password) and return the username
        try:
            decoded_credentials = base64.b64decode(base64_credentials).decode('utf-8')
            username, password = decoded_credentials.split(":")
            # Here, we just return the username for demonstration purposes
            # In a real-world app, you would validate the username/password against a user store
            return username
        except Exception:
            return None
