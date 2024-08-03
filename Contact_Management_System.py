import re
import json

# Menu Options
def display_menu():
    print("Welcome to the Contact Management System")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Sort contacts")
    print("9. Backup contacts")
    print("10. Restore contacts from backup")
    print("11. Quit")


# Store contact information
contacts = {}

def add_contact(unique_id, name, phone, email, additional_info, categories, custom_fields):
    contacts[unique_id] = {
        'name': name,
        'phone': phone,
        'email': email,
        'additional_info': additional_info,
        'categories': categories,
        'custom_fields': custom_fields
    }


# Adding a new contact
def add_new_contact():
    unique_id = input("Enter unique identifier (phone number or email): ")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    additional_info = input("Enter additional information (address, notes): ")
    categories = input("Enter categories (comma-separated): ").split(',')
    custom_fields = {}
    while True:
        field_name = input("Enter custom field name (or 'done' to finish): ")
        if field_name.lower() == 'done':
            break
        field_value = input(f"Enter value for {field_name}: ")
        custom_fields[field_name] = field_value
    add_contact(unique_id, name, phone, email, additional_info, categories, custom_fields)
    print("Contact added successfully!")


# Editing an existing contact
def edit_contact():
    unique_id = input("Enter unique identifier of the contact to edit: ")
    if unique_id in contacts:
        contact = contacts[unique_id]
        print("Editing contact:", contact)
        name = input(f"Enter new name ({contact['name']}): ") or contact['name']
        phone = input(f"Enter new phone number ({contact['phone']}): ") or contact['phone']
        email = input(f"Enter new email address ({contact['email']}): ") or contact['email']
        additional_info = input(f"Enter new additional information ({contact['additional_info']}): ") or contact['additional_info']
        categories = input(f"Enter new categories (comma-separated) ({', '.join(contact['categories'])}): ").split(',') or contact['categories']
        custom_fields = contact['custom_fields']
        while True:
            field_name = input("Enter custom field name to update (or 'done' to finish): ")
            if field_name.lower() == 'done':
                break
            field_value = input(f"Enter new value for {field_name} ({custom_fields.get(field_name, 'not set')}): ")
            custom_fields[field_name] = field_value
        add_contact(unique_id, name, phone, email, additional_info, categories, custom_fields)
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

# Deleting a contact
def delete_contact():
    unique_id = input("Enter unique identifier of the contact to delete: ")
    if unique_id in contacts:
        del contacts[unique_id]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

# Searching for a contact 
def search_contact():
    search_term = input("Enter name, phone number, email, or additional info to search: ")
    found = False
    for unique_id, details in contacts.items():
        if (search_term.lower() in details['name'].lower() or
            search_term.lower() in details['phone'].lower() or
            search_term.lower() in details['email'].lower() or
            search_term.lower() in details['additional_info'].lower()):
            print(f"ID: {unique_id}, Details: {details}")
            found = True
    if not found:
        print("Contact not found!")

# Sorting contacts
def sort_contacts():
    print("Sort by: 1. Name, 2. Unique ID")
    choice = input("Select sorting option: ")
    if choice == '1':
        sorted_contacts = dict(sorted(contacts.items(), key=lambda item: item[1]['name'].lower()))
    elif choice == '2':
        sorted_contacts = dict(sorted(contacts.items()))
    else:
        print("Invalid choice! Sorting by unique ID.")
        sorted_contacts = dict(sorted(contacts.items()))
    for unique_id, details in sorted_contacts.items():
        print(f"ID: {unique_id}, Details: {details}")

# Backup contacts
def backup_contacts(filename):
    with open(filename, 'w') as file:
        json.dump(contacts, file)
    print("Backup created successfully!")

# Restoring contacts from backup
def restore_contacts(filename):
    try:
        with open(filename, 'r') as file:
            global contacts
            contacts = json.load(file)
        print("Contacts restored successfully!")
    except FileNotFoundError:
        print("Backup file not found!")

# Displaying all contacts
def display_all_contacts():
    if contacts:
        print("Listing all contacts:")
        for unique_id, details in contacts.items():
            categories = ', '.join(details['categories'])
            custom_fields = ', '.join(f"{key}: {value}" for key, value in details['custom_fields'].items())
            print(f"ID: {unique_id}")
            print(f"  Name: {details['name']}")
            print(f"  Phone: {details['phone']}")
            print(f"  Email: {details['email']}")
            print(f"  Additional Info: {details['additional_info']}")
            print(f"  Categories: {categories}")
            print(f"  Custom Fields: {custom_fields}")
            print("-" * 40)  # Separator for better readability
    else:
        print("No contacts found!")


# Exporting contacts to a text file
def export_contacts(filename):
    with open(filename, 'w') as file:
        for unique_id, details in contacts.items():
            file.write(f"{unique_id},{details['name']},{details['phone']},{details['email']},{details['additional_info']}\n")
    print("Contacts exported successfully!")

# Importing contacts from a text file
def import_contacts(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) < 5:
                    print(f"Skipping malformed line: {line.strip()}")
                    continue
                unique_id, name, phone, email, additional_info = parts[:5]
                categories = parts[5].split(',') if len(parts) > 5 else []
                custom_fields = {}
                # Handle additional custom fields if needed
                add_contact(unique_id, name, phone, email, additional_info, categories, custom_fields)
        print("Contacts imported successfully!")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"An error occurred during import: {e}")
# Implement input validation using regex
def validate_input(pattern, input_str):
    return re.match(pattern, input_str) is not None

# Example validation patterns
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
phone_pattern = r'^\+?1?\d{9,15}$'

# Error handling
def perform_action():
    while True:
        display_menu()
        choice = input("Select an option: ")
        try:
            if choice == '1':
                add_new_contact()
            elif choice == '2':
                edit_contact()
            elif choice == '3':
                delete_contact()
            elif choice == '4':
                search_contact()
            elif choice == '5':
                display_all_contacts()
            elif choice == '6':
                filename = input("Enter filename to export contacts: ")
                export_contacts(filename)
            elif choice == '7':
                filename = input("Enter filename to import contacts: ")
                import_contacts(filename)
            elif choice == '8':
                sort_contacts()
            elif choice == '9':
                filename = input("Enter filename to backup contacts: ")
                backup_contacts(filename)
            elif choice == '10':
                filename = input("Enter filename to restore contacts from backup: ")
                restore_contacts(filename)
            elif choice == '11':
                print("Exiting the Contact Management System. Goodbye!")
                break
            else:
                print("Invalid choice! Please select a valid option.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print("Action completed.")

if __name__ == "__main__":
    perform_action()
