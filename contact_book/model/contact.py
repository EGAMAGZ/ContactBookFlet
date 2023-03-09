from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Contact:
    name: str
    last_name: str
    phone: str
    email: str
    _id: Optional[None] = field(default=None)
