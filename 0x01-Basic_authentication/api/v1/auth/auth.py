from typing import List

class Auth:
    """Auth class to manage API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if a path is in the excluded paths."""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        return path not in [ep[:-1] if ep.endswith('/') else ep for ep in excluded_paths]

    def authorization_header(self, request=None) -> str:
        """Retrieve the Authorization header."""
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None):
        """Retrieve the current user."""
        return None

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
        # This is a simple example; in a real case, you'd decode and validate credentials
        return base64_credentials
