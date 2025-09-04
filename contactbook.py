contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for i, c in enumerate(contacts, 1):
            print(i, "-", c["name"], ":", c["phone"])

def search_contact():
    key = input("Enter name or phone to search: ")
    found = False
    for c in contacts:
        if c["name"] == key or c["phone"] == key:
            print("Name:", c["name"])
            print("Phone:", c["phone"])
            print("Email:", c["email"])
            print("Address:", c["address"])
            found = True
    if not found:
        print("No contact found.")

def update_contact():
    key = input("Enter name of contact to update: ")
    for c in contacts:
        if c["name"] == key:
            c["phone"] = input("Enter new phone: ")
            c["email"] = input("Enter new email: ")
            c["address"] = input("Enter new address: ")
            print("Contact updated!")
            return
    print("Contact not found.")

def delete_contact():
    key = input("Enter name of contact to delete: ")
    for c in contacts:
        if c["name"] == key:
            contacts.remove(c)
            print("Contact deleted!")
            return
    print("Contact not found.")

while True:
    print("\n--- Contact Management ---")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")
