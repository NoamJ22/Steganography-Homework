text = "the quick brown fox jumps over the lazy dog near the quiet riverbank on an afternoon full of sun"
word = "null"

#גרסה של להחביא את המסר בין הטקסט
def insertMessage(text, word):
    split = text.split()
    for i in range(len(word)):
        split[i*3] = split[i*3][:1] + word[i] + split[i*3][1:]

    return ' '.join(split)

def reconstructMessage(text):
    split = text.split()
    message = ""
    i = 0
    while (i*3 < len(split)):
        message += split[i*3][1]
        message += " "
        i+=1

    return message


broken_text = insertMessage(text, word)
print(broken_text)
message = reconstructMessage(broken_text)
print(message)

#גרדה של להחביא את המסר בטקסט
def hideMessage(text, word):
    word.lower()
    text.lower()
    index = 0
    for c in word:
        index = text.find(c, index)
        text = text[:index] + c.upper() + text[index + 1:]
    return text

def findMessage(text):
    message = [c for c in text if c.isupper()]
    message = ''.join(message)
    return message.lower()

hidden_text = hideMessage(text, word)
print(hidden_text)
hidden_word = findMessage(hidden_text)
print(hidden_word)

