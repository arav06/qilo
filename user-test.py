import getpass as gp
import random
import string

username = gp.getuser()
id = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=5))

print(f"{username}@qilo-{id}")
