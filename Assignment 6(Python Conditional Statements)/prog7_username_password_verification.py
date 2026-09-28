"""
Program 7: Username & password verification.
"""

# Stored credentials database (simulated)
CREDENTIALS_DB = {
    "admin": "admin123",
    "krish": "secretpass",
    "student": "pass2026"
}

def verify_login(username, password):
    if username in CREDENTIALS_DB:
        if CREDENTIALS_DB[username] == password:
            print(f"Login Successful! Welcome back, {username}.")
            return True
        else:
            print(f"Login Failed! Incorrect password for user '{username}'.")
            return False
    else:
        print(f"Login Failed! Username '{username}' not found.")
        return False


def main():
    print("--- Program 7: Username and Password Verification ---")
    
    print("Attempt 1:")
    verify_login("krish", "secretpass")
    
    print("\nAttempt 2:")
    verify_login("krish", "wrongpass")
    
    print("\nAttempt 3:")
    verify_login("unknown_user", "pass123")


if __name__ == "__main__":
    main()
