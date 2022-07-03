"""

"""

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"A really secret message. Not for prying eyes.")
print(token)

untoken = f.decrypt(token)
print(untoken)

