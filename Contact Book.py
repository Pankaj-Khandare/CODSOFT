class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email} | {self.address}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    
    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        address = input("Enter contact address: ")
        
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print("Contact added successfully!")

    
    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                print(contact)

    
    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        found_contacts = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone]
        
        if found_contacts:
            print("Search Results:")
            for contact in found_contacts:
                print(contact)
        else:
            print("No contact found matching your search.")

    
    def update_contact(self):
        name_to_update = input("Enter the name of the contact to update: ")
        contact_found = False
        
        for contact in self.contacts:
            if contact.name.lower() == name_to_update.lower():
                contact_found = True
                print(f"Found: {contact}")
                contact.name = input("Enter new name: ")
                contact.phone = input("Enter new phone number: ")
                contact.email = input("Enter new email address: ")
                contact.address = input("Enter new address: ")
                print("Contact updated successfully!")
                break
        
        if not contact_found:
            print("Contact not found.")

    
    def delete_contact(self):
        name_to_delete = input("Enter the name of the contact to delete: ")
        contact_found = False
        
        for contact in self.contacts:
            if contact.name.lower() == name_to_delete.lower():
                contact_found = True
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                break
        
        if not contact_found:
            print("Contact not found.")


def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")


def main():
    contact_book = ContactBook()

    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            contact_book.add_contact()
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            contact_book.search_contact()
        elif choice == "4":
            contact_book.update_contact()
        elif choice == "5":
            contact_book.delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")



if __name__ == "__main__":
    main()
