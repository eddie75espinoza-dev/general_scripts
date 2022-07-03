import os
import random
import secrets 

# With OS
print("Con OS")
print(os.urandom(12))

# With Random
ch_lower = "abcdefghijklmnopqrstuvwxyz"
ch_upper = ch_lower.upper()
numbers = "0123456789"
symbols = "$%*,.;:/-&#@"

ch_all = ch_upper+ch_lower+numbers+symbols
length = 12
passw = "".join(random.sample(ch_all,length))
print("Con Random")
print(passw)

# With Secrets
print("Con Secrets")
print(secrets.token_urlsafe(12))
