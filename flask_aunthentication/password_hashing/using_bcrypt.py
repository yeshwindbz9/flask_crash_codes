from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
password = input("Enter a password: ")
hashed_password = bcrypt.generate_password_hash(password=password)
print("Hashed password: ", hashed_password)
check = input("Enter password to recheck: ")
check = bcrypt.check_password_hash(hashed_password, check)
print("Password check result:", check)