import pickle


# it's a contact class defining contacts
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

# Function to load contacts from file (using pickle)
def load_contacts():
    try:
        with open("contacts.pkl", "rb") as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return []

# Function to save contacts to file
def save_contacts(contacts):
    with open("contacts.pkl", "wb") as file:
        pickle.dump(contacts, file)

# Add a new contact
def add_contact(contacts):
    print("\nAdd a New Contact:")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    new_contact = Contact(name, phone, email, address)
    contacts.append(new_contact)
    save_contacts(contacts)
    print(f"\nContact for {name} added successfully!")

# View all contacts
def view_contacts(contacts):
    print("\nList of Contacts:")
    if contacts:
        for contact in contacts:
            print(contact)
    else:
        print("No contacts found.")

# Search for a contact by name or phone number
def search_contact(contacts):
    search_term = input("\nEnter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_term in contact.name or search_term in contact.phone]
    
    if found_contacts:
        print("\nSearch Results:")
        for contact in found_contacts:
            print(contact)
    else:
        print("No contact found with that name or phone number.")

# Update a contact's details
def update_contact(contacts):
    search_term = input("\nEnter name or phone number of the contact to update: ")
    found_contacts = [contact for contact in contacts if search_term in contact.name or search_term in contact.phone]
    
    if found_contacts:
        print("\nFound Contact(s) to Update:")
        for contact in found_contacts:
            print(contact)
        
        contact_to_update = found_contacts[0]
        print(f"\nUpdating details for {contact_to_update.name}:")
        contact_to_update.name = input(f"Enter new name (current: {contact_to_update.name}): ") or contact_to_update.name
        contact_to_update.phone = input(f"Enter new phone number (current: {contact_to_update.phone}): ") or contact_to_update.phone
        contact_to_update.email = input(f"Enter new email (current: {contact_to_update.email}): ") or contact_to_update.email
        contact_to_update.address = input(f"Enter new address (current: {contact_to_update.address}): ") or contact_to_update.address
        
        save_contacts(contacts)
        print(f"\nContact for {contact_to_update.name} updated successfully!")
    else:
        print("No contact found to update.")

# Delete a contact
def delete_contact(contacts):
    search_term = input("\nEnter name or phone number of the contact to delete: ")
    found_contacts = [contact for contact in contacts if search_term in contact.name or search_term in contact.phone]
    
    if found_contacts:
        print("\nFound Contact(s) to Delete:")
        for contact in found_contacts:
            print(contact)
        
        contact_to_delete = found_contacts[0]
        confirm = input(f"\nAre you sure you want to delete the contact for {contact_to_delete.name}? (yes/no): ").lower()
        
        if confirm == "yes":
            contacts.remove(contact_to_delete)
            save_contacts(contacts)
            print(f"\nContact for {contact_to_delete.name} deleted successfully!")
        else:
            print("Deletion cancelled.")
    else:
        print("No contact found to delete.")

# Main menu for the contact book
def main():
    contacts = load_contacts()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("\nChoose an option (1-6): ")
        
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
            print("\nGoodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
