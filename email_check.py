def is_valid_email(s):
    has_at = "@" in s
    has_dot = "." in s
    return has_at and has_dot
