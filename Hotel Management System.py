rooms = {
    101: {"type": "Single", "price": 500, "status": "Available", "name": "", "contact": "", "days": 0, "services": []},
    102: {"type": "Double", "price": 900, "status": "Available", "name": "", "contact": "", "days": 0, "services": []},
    104: {"type": "Suite", "price": 1500, "status": "Available", "name": "", "contact": "", "days": 0, "services": []},
    109: {"type": "Deluxe", "price": 2000, "status": "Available", "name": "", "contact": "", "days": 0, "services": []},
    105: {"type": "Suite", "price": 1500, "status": "Available", "name": "", "contact": "", "days": 0, "services": []},
    110: {"type": "Single", "price": 500, "status": "Available", "name": "", "contact": "", "days": 0, "services": []},
    150: {"type": "Presidential", "price": 3000, "status": "Available", "name": "", "contact": "", "days": 0, "services": []},
    222: {"type": "Deluxe", "price": 2000, "status": "Available", "name": "", "contact": "", "days": 0, "services": []},
    901: {"type": "Double", "price": 900, "status": "Available", "name": "", "contact": "", "days": 0, "services": []},
    200: {"type": "Single", "price": 500, "status": "Available", "name": "", "contact": "", "days": 0, "services": []},
}

facilities = {
    "breakfast": 200,
    "lunch": 400,
    "dinner": 600,
    "luxury_dinner": 1200,
    "swimming_pool": 300,
    "spa": 1000,
    "cinema": 500,
    "gym": 200,
    "laundry": 150
}

room_facilities = {
    "Single": ["breakfast"],
    "Double": ["breakfast", "gym"],
    "Deluxe": ["breakfast", "gym", "swimming_pool"],
    "Suite": ["breakfast", "lunch", "gym", "swimming_pool"],
    "Presidential": [
        "breakfast", "lunch", "dinner", "luxury_dinner",
        "swimming_pool", "spa", "cinema", "gym", "laundry"
    ]
}

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^      ")
print("                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^               ")
print("                                                 WELCOME TO THE HARBOR HOUSE                        ")
print("                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^             ")
print("                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^      ")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("\n")
print("   ==========HOTEL RESERVATION SYSTEM=========               ")

def menu():
    print("Press A for Admin")
    print("Press C for Customer")
    print("Press E to Exit")

def customer_menu():
    print("\n===== CUSTOMER PORTAL =====")
    print("1. Book Room")
    print("2. Check-out")
    print("3. View Room Info")
    print("4. Back to Main Menu")

def admin_menu():
    print("\n===== ADMIN MENU =====")
    print("1. ADD ROOM")
    print("2. UPDATE ROOM INFO")
    print("3. DELETE ROOM")
    print("4. VIEW ALL ROOMS")
    print("5. VIEW ALL CUSTOMERS")
    print("6. LOGOUT")

def room_list():
    print("\nRoom Number | Type          | Price | Status")
    print("-" * 50)
    for r, i in rooms.items():
        print(f"{r} | {i['type']} | {i['price']} | {i['status']}")

def update_menu():
    print("\n1. Update Price")
    print("2. Update Type")
    print("3. Update Room Number")
    print("4. Update Status")

while True:
    menu()
    choice = input("Enter your choice: ").upper()
    if choice == "C":
        customer_menu()
        c = int(input("Enter your choice: "))
        if c == 1:
            room_list()
            rno = int(input("Enter room number you want to book: "))
            if rno in rooms:
                if rooms[rno]["status"] == "Available":
                    name = input("Enter your name: ")
                    contact = input("Enter your contact number: ")
                    days = int(input("How many days you want to stay? "))

                    rooms[rno]["name"] = name
                    rooms[rno]["contact"] = contact
                    rooms[rno]["days"] = days
                    rooms[rno]["status"] = "Booked"

                    room_type = rooms[rno]["type"]
                    selected_facilities = room_facilities.get(room_type, []).copy()
                    rooms[rno]["services"] = selected_facilities


                    print("\nFacilities included in your room by default:")
                    for f in selected_facilities:
                        print("-", f)

                    add_fac = input("\nDo you want to add extra facilities? (y/n): ").lower()
                    if add_fac == "y":
                        print("\nAvailable Extra Facilities:")
                        for f_name, f_price in facilities.items():
                            if f_name not in selected_facilities:
                                print(f"- {f_name} ({f_price} per day)")
                        while True:
                            extra = input("Enter facility to add (or 'done' to finish): ").lower()
                            if extra == "done":
                                break
                            elif extra in facilities and extra not in selected_facilities:
                                selected_facilities.append(extra)
                                print(f"{extra} added.")
                            else:
                                print("Invalid or already added facility.")


                    rooms[rno]["services"] = selected_facilities


                    facility_cost = sum(facilities[f] * days for f in selected_facilities)
                    room_cost = rooms[rno]["price"] * days
                    total = room_cost + facility_cost

                    print("\nRoom booked successfully!")
                    print("Customer:", name)
                    print("Contact:", contact)
                    print("Room Type:", rooms[rno]["type"])
                    print("Price per night:", rooms[rno]["price"])
                    print("Facilities Used:")
                    for f in selected_facilities:
                        print("-", f)
                    print("Facility Cost:", facility_cost)
                    print("Total Amount:", total)
                else:
                    print("Sorry! Room already booked.")
            else:
                print("Room not found.")

        elif c == 2:
            name = input("Enter your name for checkout: ")
            found = False
            for rno, info in rooms.items():
                if info["name"] == name:
                    found = True

                    room_cost = info["price"] * info["days"]
                    facility_cost = sum(facilities[f]*info["days"] for f in info["services"])
                    grand_total = room_cost + facility_cost

                    print("\n===== CHECKOUT DETAILS =====")
                    print("Customer Name:", info["name"])
                    print("Contact:", info["contact"])
                    print("Room Number:", rno)
                    print("Room Type:", info["type"])
                    print("Stayed Days:", info["days"])
                    print("Room Cost:", room_cost)
                    print("Facilities Used:", ', '.join(info["services"]))
                    print("Facility Cost:", facility_cost)
                    print("Total Bill:", grand_total)

                    info["status"] = "Available"
                    info["name"] = ""
                    info["contact"] = ""
                    info["days"] = 0
                    info["services"] = []

                    print("\nCheckout Successful! Thank you for staying.")
                    break
            if not found:
                print("No booking found for this name.")

        elif c == 3:
            room_list()
        elif c == 4:
            continue

    elif choice == "A":
        name = input("Enter your username: ")
        password = input("Enter your password: ")

        if name == "harbor" and password == "2005":
            print("You've logged in successfully!\n")

            while True:
                admin_menu()
                a = int(input("Enter your choice: "))
                if a == 1:
                    r = int(input("Enter new room number: "))
                    t = input("Enter room type: ")
                    p = int(input("Enter price: "))
                    rooms[r] = {"type": t, "price": p, "status": "Available", "name": "", "contact": "", "days": 0, "services": []}
                    print("Room added successfully!")
                elif a == 2:
                    room_list()
                    rno = int(input("Enter room number to update: "))
                    if rno in rooms:
                        update_menu()
                        u = int(input("Enter your choice: "))
                        if u == 1:
                            rooms[rno]["price"] = int(input("Enter new price: "))
                        elif u == 2:
                            rooms[rno]["type"] = input("Enter new type: ")
                        elif u == 3:
                            new_r = int(input("Enter new room number: "))
                            rooms[new_r] = rooms.pop(rno)
                        elif u == 4:
                            rooms[rno]["status"] = input("Enter status (Available/Booked): ")
                        else:
                            print("Invalid option!")
                    else:
                        print("Room not found!")
                elif a == 3:
                    rno = int(input("Enter room number to delete: "))
                    if rno in rooms:
                        rooms.pop(rno)
                        print("Room deleted successfully!")
                    else:
                        print("Room not found!")
                elif a == 4:
                    room_list()
                elif a == 5:
                    print("\n===== ALL CUSTOMERS =====")
                    any_customer = False
                    for rno, info in rooms.items():
                        if info["name"] != "":
                            any_customer = True
                            room_cost = info["price"] * info["days"]
                            facility_cost = sum(facilities[f]*info["days"] for f in info["services"])
                            total = room_cost + facility_cost
                            print(f"\nRoom {rno}")
                            print(f"Customer Name: {info['name']}")
                            print(f"Contact: {info['contact']}")
                            print(f"Room Type: {info['type']}")
                            print(f"Stayed Days: {info['days']}")
                            print(f"Facilities Used: {', '.join(info['services'])}")
                            print(f"Total Bill: {total}")
                            print("-" * 30)
                    if not any_customer:
                        print("No customers currently registered.")
                elif a == 6:
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice!")
        else:
            print("Wrong username or password!")

    elif choice == "E":
        print("Thank you for visiting!")
        break
    else:
        print("Invalid choice!")

    back = input("\nDo you want to go back to main menu? (Y/N): ").upper()
    if back != "Y":
        print("Thank you for visiting!")
        break
