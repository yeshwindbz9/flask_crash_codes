from werkzeug.security import generate_password_hash, check_password_hash

password = input("Enter a password: ")
hashed_password = generate_password_hash(password)
print("Hashed password:", hashed_password)
check = input("Enter password to recheck: ")
check = check_password_hash(hashed_password, check)
print("Password check result:", check)