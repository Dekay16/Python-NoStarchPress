prompt = "\nTell me something to write and I will repeat it: "
prompt += "\nEnter 'quit' to end the program. "

#flag: Used to make the program perform a number of functions until the flag is returned false.
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)


