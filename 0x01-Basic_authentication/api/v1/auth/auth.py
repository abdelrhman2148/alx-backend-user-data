from typing import List, TypeVar

class Auth:
    """Auth class to manage API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determine if a path requires authentication."""
        return False

    def authorization_header(self, request=None) -> str:
        """Retrieve the Authorization header."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieve the current user."""
        return None
