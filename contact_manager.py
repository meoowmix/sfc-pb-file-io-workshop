import json, io

"""
Note: This is designed to hold a list of contacts as a list of dictionaries.
An alternative approach is to build a "Contact" class to represent a contact.
If you would like to do that as a Bonus exercise, that would be good way
to practice using OOP and composition!
"""


class ContactManager:
    """Class to do CRUD operations on the list of contacts"""

    def __init__(self, file="data.json"):
        self.file = file
        self.contacts = []
        self.load_contacts

    def load_contacts(self):
        with io.open(self.file, 'r') as file:
             self.contacts = json.load(file)
        # if self.contacts == []:
        #     return print("No Contacts")
        # else:
        return self.contacts

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()
        print("Contact Added")

    def update_contact(self, contact_to_update):
        self.delete_contact(contact_to_update.get("id"))
        self.contacts.append(contact_to_update)
        self.save_contacts()
        print(f"Contact #{contact_to_update.get('id')} Updated")

    def delete_contact(self, id_to_delete):
        keep = []
        for contact in self.contacts:
            if contact['id'] != id_to_delete:
                keep.append(contact)
        self.contacts = keep
        self.save_contacts()
        print(f"Deleting Contact #{id_to_delete}")

    def save_contacts(self):
        with io.open(self.file, 'w') as file:
            json.dump(self.contacts, file)
