from getpass import getpass

user_name = input("Enter your Username: ")
user_password = getpass("Enter your Password: ")

print(user_name)
print(user_password)

## whithout getpass

user_name = input("Enter your Username: ")
user_password = input("Enter your Password: ")

print(user_name)
print(user_password)