import re

injection_signs = [
    "'",
    '"',
    "--",
    ";",
    "/*",
    "*/",
    "OR",
    "AND",
    "DROP",
    "UNION",
    "INSERT",
    "DELETE",
    "UPDATE",
    "SELECT",
    "EXEC",
    "SHUTDOWN",
    "WAITFOR DELAY",
    "`",
    "\\",
    "%",
    "_",
    "=",
    "<",
    ">",
    "||"
]

def detectInjection(string, signs):
    string_upper = string.upper()

    for sign in signs:
        if sign.upper() in string_upper:
            print("Injection Detected!")
            return

    print("No Injection Detected!")

# Test it
detectInjection("hi, I am", injection_signs)               
detectInjection("DROP TABLE users;", injection_signs)      
detectInjection("admin' OR 1=1 --", injection_signs)  
