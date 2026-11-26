MIN_PASSWORD_LENGTH = 10

def check_password(pw):
    return len(pw) >= MIN_PASSWORD_LENGTH
