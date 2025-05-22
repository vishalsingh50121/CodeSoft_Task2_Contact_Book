contacts = []

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email (optional): ").strip() or "N/A"
    address = input("Enter address (optional): ").strip() or "N/A"
    
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print(f"\n✅ Contact '{name}' added successfully!")

def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    print("\n--- Search Contact ---")
    query = input("Enter name or phone number: ").strip().lower()
    results = []
    
    for contact in contacts:
        if (query in contact["name"].lower()) or (query in contact["phone"]):
            results.append(contact)
    
    if not results:
        print("❌ No matching contacts found.")
    else:
        print("\nSearch Results:")
        for contact in results:
            print(f"📞 Name: {contact['name']}")
            print(f"   Phone: {contact['phone']}")
            print(f"   Email: {contact['email']}")
            print(f"   Address: {contact['address']}\n")

def update_contact():
    view_contacts()
    if not contacts:
        return
    
    try:
        contact_num = int(input("\nEnter contact number to update: ")) - 1
        if 0 <= contact_num < len(contacts):
            contact = contacts[contact_num]
            print(f"\nEditing: {contact['name']}")
            
            contact["name"] = input(f"Name ({contact['name']}): ").strip() or contact["name"]
            contact["phone"] = input(f"Phone ({contact['phone']}): ").strip() or contact["phone"]
            contact["email"] = input(f"Email ({contact['email']}): ").strip() or contact["email"]
            contact["address"] = input(f"Address ({contact['address']}): ").strip() or contact["address"]
            
            print("\n✅ Contact updated successfully!")
        else:
            print("❌ Invalid contact number!")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_contact():
    view_contacts()
    if not contacts:
        return
    
    try:
        contact_num = int(input("\nEnter contact number to delete: ")) - 1
        if 0 <= contact_num < len(contacts):
            deleted_name = contacts[contact_num]["name"]
            del contacts[contact_num]
            print(f"\n✅ Contact '{deleted_name}' deleted successfully!")
        else:
            print("❌ Invalid contact number!")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    print("\n📞 Contact Management System")
    print("---------------------------")
    
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("\nChoose an option (1-6): ").strip()
        
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
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
