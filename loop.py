# FOR, WHILE, etc.

while (condition):
    # Continue until condition is False
    print("Hello World")

#######################################

while 10 > 5:
    print("True")

#######################################

while True:
    print("Always True")

#######################################
# Password

password = "EAI"
user_input = input()

while True:
    if password == user_input:
        print("Access Granted")
        break
