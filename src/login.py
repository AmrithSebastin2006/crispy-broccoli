class Login:
    def __init__(self):
        self.users = {
            "admin": "admin123",
            "user": "password"
        }

    def authenticate(self, username, password):
        return self.users.get(username) == password


if __name__ == "__main__":
    login = Login()

    username = input("Username: ")
    password = input("Password: ")

    if login.authenticate(username, password):
        print("Login successful!")
    else:
        print("Invalid username or password.")
