prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break                   # Break: will exit the loop when condition equals true. If city = quit then break the loop.
    else:
        print(f"I'd love to go to {city.title()}!")



# Continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)