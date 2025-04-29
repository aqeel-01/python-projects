

import json

CONTACT_FILE = "contacts.json"


# load contacts from file 
def load_contacts():
    try:
        with open(CONTACT_FILE , "r") as file:
            data = json.load(file)
            return data if isinstance(data,list) else []
    except(FileNotFoundError, json.JSONDecodeError):
        return[]
  

# save contacts to file

def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


# add a new contact

def add_contact(contacts):
    name = input("Enter contact name :  ")
    phone = input("Enter phone number :   ")
    email = input("Enter email : ")
    contacts.append({"name":name, "phone":phone, "email":email})
    save_contacts(contacts)
    print("✅ Contact added sucessfully!")


# view all contacts

def view_contacts(contacts):
    if not contacts:
        print("No contacts available!")
        return
    print("\n contact list")
    for idx, contact in enumerate(contacts, start = 1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")


# search for a contact
def search_contact(contacts):
    keyword = input("enter name or phone to search:  ").lower()
    found = [c for c in contacts if keyword in c["name"].lower() or keyword in c["phone"]]
    if not found:
        print(" ❌ No contact found! ")
    else:
        print("\n  Search Results: ")
        for contact in found:
            print(f"{contact['name']} - {contact['phone']} - {contact['email']}")


# update a contact

def update_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        index= int(input("Enter the contact number to update:  ")) - 1
        if 0 <= index < len(contacts):
            contacts[index]["name"] = input("Enter new name: ")
            contacts[index]["phone"] = input("Enter new phone number: ")
            contacts[index]["email"] = input("Enter new email:  ")
            save_contacts(contacts)
            print("✅ Contact updated sucessfully!")
        else:
            print("❌ Invalid contact number!")
    except ValueError:
        print("❌ please enter a valid number! ")


# delete a contact

def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        index = int(input(" Enter the contact number to delete: ")) -1
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            save_contacts(contacts)
            print(f" contact '{deleted_contact['name']}' deleted sucessfully!")
        else:
            print(" ❌ Invalid contact number !")
    except ValueError:
        print("❌ please enter a value number !")


# main menu
def main():
    contacts = load_contacts()
    while True:
        print("\n Contact Manger ")
        print("1. Add Contact")
        print("2. View Contacts ")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice:  ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print(" Exiting Contact Manager . Goodbye!")
            break
        else:
            print("❌ Invalid choice! please enter a number between 1-6.")
        

# run the program
if __name__ == "__main__":
    main()



