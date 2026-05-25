# Restaurant Ordering System

# Menu definition
menu = {
    1: {"name": "Burger", "price": 5.00},
    2: {"name": "Fries",  "price": 3.00},
    3: {"name": "Drink",  "price": 2.00},
    4: {"name": "Pizza",  "price": 8.00},
    5: {"name": "Salad",  "price": 4.00}
}

DISCOUNT_RATE = 0.10      # 10% discount
DISCOUNT_THRESHOLD = 50.0 # discount if subtotal >= 50
TAX_RATE = 0.06           # 6% tax

def display_menu():
    print("====== RESTAURANT MENU ======")
    for num, item in menu.items():
        print(f"{num}) {item['name']} - ${item['price']:.2f}")
    print("99) Finish order")
    print("=============================")

def main():
    order = {item_num: 0 for item_num in menu}  # track quantities per item

#==============================================================================
#Devlin

    while True:
        display_menu()
        choice = input("Enter the number of the item you want to order (99 to finish): ").strip()

        # Validate numeric input
        if not choice.isdigit():
            print("Error: Please enter a numeric value (1-5 or 99).\n")
            continue

        choice = int(choice)

        # Finish ordering
        if choice == 99:
            break

        # Validate menu choice
        if choice not in menu:
            print("Error: Please enter a valid item number between 1 and 5, or 99 to finish.\n")
            continue

        # Ask for quantity
        qty_input = input(f"How many {menu[choice]['name']}(s) would you like? ").strip()
        if not qty_input.isdigit():
            print("Error: Quantity must be a positive whole number.\n")
            continue

#==============================================================================
#shawniya


        qty = int(qty_input)
        if qty <= 0:
            print("Error: Quantity must be at least 1.\n")
            continue

        # Add to order
        order[choice] += qty
        print(f"Added {qty} x {menu[choice]['name']} to your order.\n")

    # Calculate totals
    total_items = sum(order.values())
    if total_items == 0:
        print("Your order is empty. No items were selected. Goodbye!")
        return

    subtotal = 0.0
    for item_num, qty in order.items():
        if qty > 0:
            price = menu[item_num]["price"]
            subtotal += price * qty

#==============================================================================
#Mason



    # Apply discount if applicable
    discount = 0.0
    if subtotal >= DISCOUNT_THRESHOLD:
        discount = subtotal * DISCOUNT_RATE

    taxable_amount = subtotal - discount
    tax = taxable_amount * TAX_RATE
    total_due = taxable_amount + tax

    # Print final receipt
    print("\n========== FINAL RECEIPT ==========")
    print(f"{'Item':15} {'Qty':>5} {'Unit Price':>12} {'Line Total':>12}")
    print("-" * 50)

    for item_num, qty in order.items():
        if qty > 0:
            name = menu[item_num]["name"]
            unit_price = menu[item_num]["price"]
            line_total = unit_price * qty
            print(f"{name:15} {qty:>5} ${unit_price:>10.2f} ${line_total:>10.2f}")

    print("-" * 50)
    print(f"{'Subtotal:':30} ${subtotal:>10.2f}")

    if discount > 0:
        print(f"{'Discount (10%):':30} -${discount:>9.2f}")
    else:
        print(f"{'Discount:':30} ${0.00:>10.2f}")

    print(f"{'Tax (6.0%):':30} ${tax:>10.2f}")
    print(f"{'TOTAL DUE:':30} ${total_due:>10.2f}")
    print("===================================")
    print("Thank you for your order!")

if __name__ == "__main__":
    main()
