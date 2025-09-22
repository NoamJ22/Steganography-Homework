import random
import hmac
import hashlib

message = "hello"

dummy_messages = [
    "System reboot scheduled at 03:00 UTC.",
    "Payload transmission complete.",
    "Agent has entered the restricted zone.",
    "Heartbeat signal received.",
    "Node 41 is offline. Attempting reconnect...",
    "Coordinates logged: 45.4215° N, 75.6972° W.",
    "Access granted. Proceed with caution.",
    "Thermal readings are within safe limits.",
    "Backup power engaged.",
    "No anomaly detected in sector 9.",
    "Drone patrol route updated.",
    "Unauthorized signal intercepted.",
    "Security protocol initiated.",
    "Awaiting confirmation from command.",
    "Signal lost. Reacquisition in progress.",
    "Data packet #4031 received and verified.",
    "Environmental conditions nominal.",
    "Comm channel encrypted.",
    "Manual override requested.",
    "Unit 7 reporting: all clear."
]



def scramble(og_message, dummy, index):
    all_messages = []
    number = 0
    #I scramble and append all the characters, the dummy and the og, with a number indicating
    #the original word and and the original placement in the word
    for c in og_message:
        all_messages.append([c,index, number])
        number += 1

    for i in range(len(dummy)):
            number = 0
            if i == index:
                for c in dummy[i]:
                    all_messages.append([c,i,number])
                    number += 1

    return all_messages

def reassemble(scrambled, index):
    #I assemble the number back together with the 2 helping indexes
    message = ""
    message_list = []
    for char, tag, number in scrambled:
        if tag == index:
            message_list.append([char,number])
    i = 0
    while i < len(message_list):
        if i == message_list[i][1]:
            message += message_list[i][0]
        i += 1

    return message

index = random.randint(1,len(dummy_messages))

scrambled = scramble(message, dummy_messages, index)
print(scrambled)


recovered = reassemble(scrambled, index)
print("Recovered message:", recovered)