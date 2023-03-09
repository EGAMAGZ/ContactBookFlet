from typing import List, Union

from flet import (
    CircleAvatar,
    Column,
    Container,
    ContainerTapEvent,
    CrossAxisAlignment,
    IconButton,
    InputBorder,
    ListTile,
    ListView,
    MainAxisAlignment,
    Page,
    Row,
    Stack,
    Text,
    TextField,
    TextThemeStyle,
    UserControl,
    alignment,
    border_radius,
    colors,
    icons,
    padding,
)

from contact_book.model.contact import Contact
from contact_book.storage.database import db
from contact_book.storage.database.contacts_table import ContactsTable


class ContactListScreen(UserControl):
    contacts_table: ContactsTable
    contact_list: List[Contact]

    def __init__(self, page: Page) -> None:
        super().__init__()
        self.expand = True
        self.contacts_table = ContactsTable(db)
        self.contact_list = self.contacts_table.get_all()

    def contact_list_view(self) -> Union[ListView, Stack]:
        if len(self.contact_list) > 0:
            return ListView(
                expand=1,
                controls=[
                    ListTile(
                        leading=CircleAvatar(
                            content=Text(
                                value=contact.name[0] if contact.name else "?",
                            ),
                        ),
                        title=Text(
                            value=contact.name
                        ),
                    )
                    for contact in self.contact_list
                ],
            )
        else:
            return Stack(
                expand=1,
                controls=[
                    Container(
                        Column(
                            tight=True,
                            controls=[
                                IconButton(
                                    icon=icons.PERSON_ADD,
                                    icon_size=48,
                                    bgcolor=colors.PRIMARY,
                                    icon_color=colors.ON_PRIMARY,
                                    on_click=self.on_click_new_contact,
                                ),
                                Text(
                                    value=(
                                        "No contacts yet. Click to add a new contact."
                                    ),
                                    style=TextThemeStyle.HEADLINE_SMALL,
                                ),
                            ],
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                        ),
                        alignment=alignment.center,
                    )
                ],
            )

    def on_click_new_contact(self, event: ContainerTapEvent) -> None:
        self.page.go("/new-contact")

    def build(self):
        return Column(
            controls=[
                Row(
                    controls=[
                        IconButton(
                            icon=icons.PERSON,
                            bgcolor=colors.PRIMARY,
                            icon_color=colors.ON_PRIMARY,
                        ),
                        Container(
                            expand=True,
                            bgcolor=colors.PRIMARY,
                            content=Row(
                                controls=[
                                    Text(
                                        value="My Contacts",
                                        color=colors.ON_PRIMARY,
                                        style=TextThemeStyle.HEADLINE_SMALL,
                                    ),
                                    IconButton(
                                        icon=icons.SETTINGS,
                                        icon_color=colors.ON_PRIMARY,
                                        tooltip="Settings",
                                    ),
                                ],
                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            padding=padding.symmetric(horizontal=16),
                            border_radius=border_radius.all(24),
                        ),
                    ]
                ),
                TextField(
                    value="",
                    border=InputBorder.NONE,
                    filled=True,
                    hint_text="Search...",
                    prefix_icon=icons.SEARCH,
                    multiline=False,
                ),
                self.contact_list_view(),
            ]
        )
