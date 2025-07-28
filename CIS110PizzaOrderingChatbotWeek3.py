print("Hello, my name is Alex your virtual assistant. I will help you order a pizza!")
print("When you place your order with me, make sure you press ENTER after each request")
userName = input("\nEnter your name:  ")
print(f"\nHello,  {userName}. Nice to meet you!")

size = input("\nWhat size do you want? Enter small, medium, or large:  ")
flavor = input("\nEnter the flavor of the pizza:  ")
crustType = input("\nWhat type of crust would you like:  ")
quantity = input("\nHow many pizzas would you like to order? Enter a numerical value:  ")
quantity = int(quantity)
method = input("\nIs this carry out delivery?:  ")

salesTax = 1.1
pizzaCost = 14.99
total = (pizzaCost * quantity) * salesTax

print("-" * 10)
print(f"Thank You, {userName} , for your order.")
print(f"Your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs ${total:,.2f}.")
print("-" * 10)
print("Have a great day!")