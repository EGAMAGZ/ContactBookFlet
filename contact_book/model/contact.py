from dataclasses import dataclass


@dataclass
class Contact:
    _id: str | None
    first_name: str
    last_name: str
    phone_number: str
    email: str
