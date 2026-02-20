cart = [
    {"item": "Laptop", "price": 1000},
    {"item": "Mouse", "price": 50},
    {"item": "Monitor", "price": 300},
    {"item": "Keyboard", "price": 80}
]

total = 0
for product in cart:
    total += product["price"]

if total > 500:
    discount = total * 0.10
    final_price = total - discount
    print(f"Original Total: ${total}")
    print(f"10% Discount Applied: -${discount}")
    print(f"Final Total: ${final_price}")
else:
    print(f"Total: ${total} (No discount applied)")