class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address


contacts = []


def add_contact():
    """Prompts the user for the contact's details and adds a new contact to the list of contacts."""

    # Prompt the user for the contact's details.
    name = input("Enter the contact's name: ")
    phone_number = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    address = input("Enter the contact's address: ")

    # Create a new contact object.
    contact = Contact(name, phone_number, email, address)

    # Add the contact to the list of contacts.
    contacts.append(contact)

    # Print a success message.
    print("Contact added successfully!")


def view_contact_list():
    """Displays a list of all saved contacts with names and phone numbers."""

    print("Contact List:")
    for contact in contacts:
        print(f"{contact.name}: {contact.phone_number}")


def search_contact():
    """Prompts the user for a search term and finds all contacts that match the search term."""

    # Prompt the user for the search term.
    search_term = input("Enter the contact name or phone number to search: ")

    # Find all contacts that match the search term.
    matching_contacts = []
    for contact in contacts:
        if search_term in contact.name or search_term in contact.phone_number:
            matching_contacts.append(contact)

    # If there are any matching contacts, display them.
    if matching_contacts:
        print("Matching contacts:")
        for contact in matching_contacts:
            print(f"{contact.name}: {contact.phone_number}")
    else:
        print("No contacts found.")


def update_contact():
    """Prompts the user for the name of the contact to update and allows the user to update the contact's details."""

    # Prompt the user for the name of the contact to update.
    contact_name = input("Enter the name of the contact to update: ")

    # Find the contact to update.
    contact = None
    for contact in contacts:
        if contact.name == contact_name:
            contact = contact
            break

    # If the contact to update was found, prompt the user for the new details.
    if contact:
        new_name = input("Enter the new name for the contact: ")
        new_phone_number = input("Enter the new phone number for the contact: ")
        new_email = input("Enter the new email address for the contact: ")
        new_address = input("Enter the new address for the contact: ")

        # Update the contact's details.
        contact.name = new_name
        contact.phone_number = new_phone_number
        contact.email = new_email
        contact.address = new_address

        # Print a success message.
        print("Contact updated successfully!")
    else:
        print("Contact not found.")


def delete_contact():
    """Prompts the user for the name of the contact to delete and removes the contact from the list of contacts."""

    # Prompt the user for the name of the contact to delete.
    contact_name = input("Enter the name of the contact to delete: ")

    # Find the contact to delete.
    contact = None
    for contact in contacts:
        if contact.name == contact_name:
            contact = contact
            break

    # If the contact to delete was found, remove it from the list of contacts.
    if contact:
        contacts.remove(contact)

        # Print a success message.
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


def main_menu():
    """Displays the main menu and allows the user to choose an option."""

    print("Welcome to the Contact Book!")
    print("Please choose an option:")
    print("1. Add contact")
    print("2. View contact list")
    print("3. Search contact
