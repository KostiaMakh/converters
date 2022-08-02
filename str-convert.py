import hashlib


# String hashing
def hash_sting(a):
    hashed_str = hashlib.sha1(str(a).encode())
    return hashed_str.hexdigest()


print(hash_sting('Python Bootcamp'))


