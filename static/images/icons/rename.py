import os

for f in os.listdir():
    new_name = f.lower()
    os.rename(f, new_name)
