class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Phone:📞 {self.phone}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        contact = Contact(name, phone)
        self.contacts.append(contact)
        print("✅Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nSaved Contacts:")
            for contact in self.contacts:
                print(contact)

    def search_contact(self, name):
        found = False
        print(f"\n🔍 Searching for '{name}'..."
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("✅Contact found:")
                print(contact)
                found = True
                break
        if not found:
            print("❌ Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
        print("❌ Contact not found.")


def main():
    book = ContactBook()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact by Name")
        print("4. Delete Contact by Name")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            book.add_contact(name, phone)
        elif choice == '2':
            book.view_contacts()
        elif choice == '3':
            name = input("Enter the name to search: ")
            book.search_contact(name)
        elif choice == '4':
            name = input("Enter the name to delete: ")
            book.delete_contact(name)
        elif choice == '5':
            print("👋Exiting Contact Book. Goodbye!")
            break
        else:
            print("⚠️Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
