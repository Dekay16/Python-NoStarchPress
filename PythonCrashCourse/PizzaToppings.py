prompt = "\nWhat toppings would you like on the pizza?: "
prompt += "\nEnter 'done' when satisified with your order."

active = True
while active:
    order = input(prompt)
    order_list = []

    if order == 'done':
        active = False
    else:
        print("Pizza with:\n ")
        print(order_list.append(order.title()))

        #Not working, trying to get it to take input each time to add to the list.