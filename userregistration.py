class UserRegistration:
    users = {}   # stores username: password

    @classmethod
    def register(cls):
        try:
            username = input("Enter username: ").strip()
            if username == "":
                raise ValueError("Username cannot be empty")

            if username in cls.users:
                raise Exception("Username already exists")

            password = input("Enter password: ").strip()
            if len(password) < 4:
                raise ValueError("Password must be at least 4 characters")

            cls.users[username] = password
            print("Registration successful")

        except Exception as e:
            print("Error:", e)

    @classmethod
    def login(cls):
        try:
            username = input("Enter username: ")
            password = input("Enter password: ")

            if username not in cls.users:
                raise Exception("User not registered")

            if cls.users[username] != password:
                raise ValueError("Incorrect password")

            print("Login successful")

        except Exception as e:
            print("Error:", e)


def main():
    while True:
        print("\n--- User Registration System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                UserRegistration.register()
            elif choice == 2:
                UserRegistration.login()
            elif choice == 3:
                print("Thank you for using the system")
                break
            else:
                print("Invalid option")

        except ValueError:
            print("Please enter a valid number")


if __name__ == "__main__":
    main()
