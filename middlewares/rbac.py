roles_permissions = {
    "admin": ["read", "write", "delete"],
    "user": ["read"],
}

def has_permission(role, action):
    """Check if a role has a specific permission."""
    return action in roles_permissions.get(role, [])
  
