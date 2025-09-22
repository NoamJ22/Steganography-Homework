import hashlib

text = "message"

hashed = hashlib.sha256(text.encode()).hexdigest()

print(hashed)

text = "messages"

second_hash = hashlib.sha256(text.encode()).hexdigest()
print(second_hash)
print(second_hash == hashed)