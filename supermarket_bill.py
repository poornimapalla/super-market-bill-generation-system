# Super Market Bill Generation System

items = []


def add_item():
    print("\n========== ADD ITEM ==========")

    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    total = quantity * price

    item = {
        "name": name,
        "quantity": quantity,
        "price": price,
        "total": total
    }

    items.append(item)

    print("Item added successfully!")


def view_items():
    if len(items) == 0:
        print("\nNo items added yet.")
        return

    print("\n========== ITEMS ==========")

    for item in items:
        print("--------------------------------")
        print("Item     :", item["name"])
        print("Quantity :", item["quantity"])
        print("Price    : ₹{:.2f}".format(item["price"]))
        print("Total    : ₹{:.2f}".format(item["total"]))


def generate_bill():
    if len(items) == 0:
        print("\nNo items available.")
        return

    subtotal = 0

    print("\n==========================================")
    print("          SUPER MARKET BILL")
    print("==========================================")

    print("Item\tQty\tPrice\tTotal")
    print("------------------------------------------")

    for item in items:
        print(
            item["name"],
            "\t",
            item["quantity"],
            "\t",
            "₹{:.2f}".format(item["price"]),
            "\t",
            "₹{:.2f}".format(item["total"])
        )

        subtotal += item["total"]

    discount = 0

    if subtotal >= 5000:
        discount = subtotal * 0.10
    elif subtotal >= 2000:
        discount = subtotal * 0.05

    after_discount = subtotal - discount

    tax = after_discount * 0.05

    final_amount = after_discount + tax

    print("------------------------------------------")
    print("Subtotal       : ₹{:.2f}".format(subtotal))
    print("Discount       : ₹{:.2f}".format(discount))
    print("Tax (5%)       : ₹{:.2f}".format(tax))
    print("Final Amount   : ₹{:.2f}".format(final_amount))
    print("==========================================")


while True:

    print("\n==========================================")
    print("       SUPER MARKET BILL SYSTEM")
    print("==========================================")
    print("1. Add Item")
    print("2. View Items")
    print("3. Generate Bill")
    print("4. Exit")
    print("==========================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_item()

    elif choice == "2":
        view_items()

    elif choice == "3":
        generate_bill()

    elif choice == "4":
        print("\nThank you for shopping!")
        break

    else:
        print("\nInvalid choice! Please enter 1 to 4.")