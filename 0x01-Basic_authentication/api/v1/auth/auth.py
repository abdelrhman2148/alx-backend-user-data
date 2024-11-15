def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
    """Check if a path is in the excluded paths."""
    if path is None or excluded_paths is None or len(excluded_paths) == 0:
        return True

    # Normalize the path to ensure consistency
    if path[-1] != '/':
        path += '/'

    # Check if path matches any in excluded_paths
    for excluded_path in excluded_paths:
        if excluded_path.endswith('/') and excluded_path[:-1] == path[:-1]:
            return False
        if excluded_path == path:
            return False

    return True
