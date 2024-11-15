from typing import List, TypeVar

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
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieve the current user."""
        return None
