menu = {
    "burger": 500,
    "pizza": 1200,
    "fries": 300,
    "cola": 150,
    "ice cream": 250,
    "fried chicken": 500
}

total = 0

print("==== MENU ====")

for item, price in menu.items():
    print(f"{item.title()} - Rs {price}")

print("\nType 'end' when you're finished ordering.\n")

while True:
    order = input("What would you like? ").lower()

    if order == "end":
        break

    if order in menu:
        total += menu[order]
        print(f"Added {order.title()} - Rs {menu[order]}")
    else:
        print("Sorry, we don't have that item.")

print(f"\nYour total bill is Rs {total}")