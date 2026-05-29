import json
contacts = {}

#Add Contact Function
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    group = input("Enter Group: ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "group": group
    }

    print("Contact Added Successfully!")

#View Contacts Function
def display_contacts():
    if not contacts:
        print("No Contacts Found")
        return

    for name, details in contacts.items():
        print("\nName:", name)
        print("Phone:", details["phone"])
        print("Email:", details["email"])
        print("Group:", details["group"])

#Search Contact Function
def search_contact():
    name = input("Enter Name To Search: ")

    if name in contacts:
        print(contacts[name])
    else:
        print("Contact Not Found")

#Delete Contact Function
def delete_contact():
    name = input("Enter Name To Delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact Deleted")
    else:
        print("Contact Not Found")

#Save Contacts To File
def save_contacts():
    with open("contacts_data.json", "w") as file:
        json.dump(contacts, file)

    print("Contacts Saved")

#Load Contacts From File
def load_contacts():
    global contacts

    try:
        with open("contacts_data.json", "r") as file:
            contacts = json.load(file)
    except:
        contacts = {}

#Main Function
def main():

    load_contacts()

    while True:

        print("\n===== CONTACT MANAGER =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Save Contacts")
        print("6. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            display_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            delete_contact()

        elif choice == "5":
            save_contacts()

        elif choice == "6":
            save_contacts()
            print("Thankyou Visit Again Goodbye!")
            break

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
    