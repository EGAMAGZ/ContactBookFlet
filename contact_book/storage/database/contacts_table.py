from typing import List

from tinydb import TinyDB
from tinydb.table import Document

from contact_book.model.contact import Contact


class ContactsTable:
    TABLE_NAME = "contacts"

    def __init__(self, db: TinyDB):
        self.contacts_table = db.table(self.TABLE_NAME)

    def __to_contact(self, document: Document) -> Contact:
        return Contact(
            _id=document.doc_id,
            name=document["first_name"],
            last_name=document["last_name"],
            phone=document["phone_number"],
            email=document["email"],
        )

    def get_all(self) -> List[Contact]:
        contacts = self.contacts_table.all()
        return list(map(self.__to_contact, contacts))

    def add_contact(self, contact: Contact):
        self.contacts_table.insert(
            {
                "first_name": contact.name,
                "last_name": contact.last_name,
                "phone_number": contact.phone,
                "email": contact.email,
            }
        )
