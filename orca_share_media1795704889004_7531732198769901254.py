lost_items = []
found_items = []


def add_lost():
    item = input("Enter lost item: ").strip()
    if item:
        lost_items.append(item)
        print("Lost item recorded!")
    else:
        print("Item name cannot be empty.")


def add_found():
    item = input("Enter found item: ").strip()
    if item:
        found_items.append(item)
        print("Found item recorded!")
    else:
        print("Item name cannot be empty.")


def view_items():
    print("\n===== LOST ITEMS =====")
    if len(lost_items) == 0:
        print("No lost items.")
    else:
        for item in lost_items:
            print("-", item)

    print("\n===== FOUND ITEMS =====")
    if len(found_items) == 0:
        print("No found items.")
    else:
        for item in found_items:
            print("-", item)


def search_item():
    name = input("Enter item to search: ").strip().lower()
    found = False

    if not name:
        print("Please enter an item name.")
        return

    for item in lost_items + found_items:
        if name in item.lower():
            print("Item found:", item)
            found = True

    if not found:
        print("Item not found.")


def main():
    while True:
        print("\n===== FINDIT =====")
        print("1. Add Lost Item")
        print("2. Add Found Item")
        print("3. View Items")
        print("4. Search Item")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_lost()
        elif choice == "2":
            add_found()
        elif choice == "3":
            view_items()
        elif choice == "4":
            search_item()
        elif choice == "5":
            print("Thank you for using FINDIT!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
