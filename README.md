# Contact Management System

Welcome to the Contact Management System! This project is a command-line-based application that allows you to manage your contacts efficiently. You can add, edit, delete, search, display, and even categorize your contacts. Additionally, you can export and import contacts to and from a text file, sort your contacts, and back up and restore your contact data.

## Features

- **Add a new contact:** Store contact details including name, phone number, email address, additional information, categories, and custom fields.
- **Edit an existing contact:** Update the details of any existing contact.
- **Delete a contact:** Remove a contact from the system using their unique identifier.
- **Search for a contact:** Find contacts by name, phone number, email address, or additional information.
- **Display all contacts:** View all stored contacts.
- **Export contacts:** Save contacts to a text file.
- **Import contacts:** Load contacts from a text file.
- **Sort contacts:** Sort contacts by name or unique identifier.
- **Backup contacts:** Create a backup of your contacts.
- **Restore contacts:** Restore contacts from a backup file.
- **Categorize contacts:** Group contacts into categories such as friends, family, or work.
- **Custom contact fields:** Add custom fields to store additional information like birthdays or anniversaries.

## Getting Started

### Prerequisites

- Python 3 installed on your system.

### Installation

1. **Clone the repository:**
    
    Git Clone https://github.com/codeland93/backend_core_day12_homework.git
    
### Running the Application

1. **Execute the Python script:**
    ```py
    python Contact_Management_System.py
    ```

2. **Follow the on-screen instructions to navigate through the menu and use the Contact Management System:**

    - **Add a new contact:** Enter details when prompted.
    - **Edit a contact:** Enter the unique identifier of the contact you want to edit and provide new details.
    - **Delete a contact:** Enter the unique identifier of the contact you want to delete.
    - **Search for a contact:** Enter a search term (name, phone number, email, or additional information).
    - **Display all contacts:** View a list of all contacts.
    - **Export contacts:** Provide a filename to save the contacts.
    - **Import contacts:** Provide a filename to load contacts from.
    - **Sort contacts:** Choose sorting criteria (name or unique ID).
    - **Backup contacts:** Provide a filename to save the backup.
    - **Restore contacts:** Provide a filename to restore contacts from a backup.

## Examples

### Adding a Contact

```py
Enter unique identifier (phone number or email): 1234567890
Enter name: John Doe
Enter phone number: 123-456-7890
Enter email address: john.doe@example.com
Enter additional information (address, notes): 123 Elm Street
Enter categories (comma-separated): friends, work
Enter custom field name (or 'done' to finish): Birthday
Enter value for Birthday: 01/01/1980
Enter custom field name (or 'done' to finish): done
Contact added successfully!
```

```py
Enter name, phone number, email, or additional info to search: John
ID: 1234567890, Details: {'name': 'John Doe', 'phone': '123-456-7890', 'email': 'john.doe@example.com', 'additional_info': '123 Elm Street', 'categories': ['friends', 'work'], 'custom_fields': {'Birthday': '01/01/1980'}}
```