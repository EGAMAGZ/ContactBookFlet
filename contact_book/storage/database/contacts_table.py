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
            first_name=document["first_name"],
            last_name=document["last_name"],
            phone_number=document["phone_number"],
            email=document["email"],
        )

    def get_all(self) -> list[Contact]:
        contacts = self.contacts_table.all()
        return list(map(self.__to_contact, contacts))

    def add_contact(self, contact: Contact):
        self.contacts_table.insert(
            {
                "first_name": contact.first_name,
                "last_name": contact.last_name,
                "phone_number": contact.phone_number,
                "email": contact.email,
            }
        )
