from dataclasses import dataclass
from typing import Optional


@dataclass
class Contact:
    _id: Optional[None]
    first_name: str
    last_name: str
    phone_number: str
    email: str
