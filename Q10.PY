"""
10.Start with a dictionary of items and prices: {'apple': 0.5, 'bread': 2.0, 'milk': 1.5}. 

1-Allow the user to "Add" or "Remove" items from a cart. 

2-If they add an item not in the store, print an error. 

Finally, print the total bill. 
• Example Input: Add 'apple', Add 'milk' • Example Output: Total Bill: $2.0 """

dict = {
    'apple': 0.5, 
    'bread': 2.0, 
    'milk': 1.5
    }

cart = []

while True:
    option = input("choose add or remove or done : ")
    if option == "done":
        break

    item = input("Enter item name: ")

    if option == "add":
        if item in dict:
            cart.append(item)
            print(f"{item} added to cart.")
        else:
            print("Error: Item not available in store.")

    elif option == "remove":
        if item in cart:
            cart.remove(item)
            print(f"{item} removed from cart")
        else:
            print("Error: Item not in cart.")

    else:
        print("Invalid option.")

total = 0

for key in cart:
    total += dict[key]

print(f"Total Bill: ${total}")