import random

#lists of numbers and words that I will use for the confusion
phone_numbers = [
    "2025550143",
    "4155550102",
    "3105550168",
    "8325550150"
]

words = [
    "astronaut",
    "banana",
    "cypress",
    "dolphin",
    "eclipse"
]

def changeNumber(number):
    #taking a random single digit number and dividing the phone number by 2 for that amount of
    #iterations, then adding the number to the beginning of the string so I can take it later
    num = int(number)
    num_of_iter = random.randint(1,9)
    for i in range(num_of_iter):
        num /= 2
    number = str(num_of_iter) + str(num)

    #picking a random word from the list for the obfuscation
    chosen_word = words[random.randint(0,len(words)-1)]
    artLen = 0

    #jamming the chosen word int0 the phone number after every number
    for i in range(len(number)):
        if i % 2 == 1 and artLen < len(chosen_word):
            number = number[:i] + chosen_word[artLen] + number[i:]
            artLen += 1

    return number

def changeNumberBack(number):
    #first I take away all the letters from the string
    clean_number = (''.join(c for c in number if not c.isalpha()))
    #now, I pick away the number of divisions by 2 from the start of the string
    num_of_iter = int(clean_number[0])
    clean_number = clean_number[1:]
    clean_number = float(clean_number)

    #I multiply the number back into it's original form
    for i in range(num_of_iter):
        clean_number *= 2

    #convert it to int to get rid of the .0 and convert back to a string
    clean_number = int(clean_number)

    return str(clean_number)


for number in phone_numbers:
    hidden = changeNumber(number)
    print(hidden)
    hidden = changeNumberBack(hidden)
    print(hidden)

    print("\n\n")