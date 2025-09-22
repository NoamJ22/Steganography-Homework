text = "At 03:47 hours, Agents Black and Ward intercepted unauthorized movement near the perimeter of Zone 6C. Thermal scans detected two unidentified figures attempting to bypass the eastern fence using cloaking tech not yet classified by central inventory. Agent Black proceeded with silent approach while Agent Ward covered from the ridge. Upon visual confirmation, both agents initiated Protocol 9. One intruder escaped beyond visual range; the second was neutralized and recovered for interrogation."
#this is a text with 2 names in it

#the list of words I want to encrypt
names = ["Black", "Ward"]

#the key
key = "house"

#the encryption method
def encryptWord(key, word):
    encrypted = ""
    for i in range(len(word)):
        encrypted += chr(ord(word[i]) ^ ord(key[i % len(key)]))
    return encrypted

words = text.split()
encrypted_text = []

for word in words:
    #striping each word so I could find them more easily
    bare = word.strip(".,;:!?")
    if bare in names:
        encrypted_word = encryptWord(key, bare)
        encrypted_text.append(f"{encrypted_word.encode().hex()}") #translating it to hexadecimal so it could be printed in the terminal
    else:
        encrypted_text.append(word)

final_text = " ".join(encrypted_text)
print(final_text)