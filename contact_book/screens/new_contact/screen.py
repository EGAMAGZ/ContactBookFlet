from flet import (
    AlertDialog,
    AppBar,
    CircleAvatar,
    Column,
    Container,
    ControlEvent,
    FilledButton,
    Icon,
    Page,
    Ref,
    Row,
    SnackBar,
    Stack,
    Text,
    TextButton,
    TextField,
    TextThemeStyle,
    UserControl,
    View,
    alignment,
    icons,
    margin,
)

from contact_book.model.contact import Contact
from contact_book.screens.exceptions import MissingParameterError
from contact_book.storage.database import db
from contact_book.storage.database.contacts_table import ContactsTable


class NewContactScreen(UserControl):
    parent_view: View
    page: Page
    contacts_table: ContactsTable

    ref_avatar_name_text = Ref[Text]()
    ref_name_field = Ref[Text]()
    ref_last_name_field = Ref[Text]()
    ref_email_field = Ref[Text]()
    ref_phone_field = Ref[Text]()

    def __init__(self, page: Page, parent_view: View) -> None:
        super().__init__()
        self.page = page
        self.parent_view = parent_view
        self.contacts_table = ContactsTable(db)

        self.parent_view.appbar = AppBar(
                title=Text("New Contact"),
                actions=[
                    Container(
                        FilledButton(
                            text="Save",
                            on_click=self.on_save_clicked,
                        ),
                        margin=margin.symmetric(horizontal=16)
                    )
                ]
            )

    def on_save_clicked(self, event: ControlEvent) -> None:
        try:
            email = self.ref_email_field.current.value
            name = self.ref_name_field.current.value
            last_name = self.ref_last_name_field.current.value
            phone = self.ref_phone_field.current.value

            if not any([email, name, last_name, phone]):
                raise MissingParameterError()

            contact = Contact(
                email=email,
                name=name,
                last_name=last_name,
                phone=phone,
            )
            self.contacts_table.add_contact(
                contact=contact,
            )
        except MissingParameterError:
            self.show_dialog()
        else:
            self.show_succes_snackbar()
            self.page.go("/")

    def show_succes_snackbar(self) -> None:
        self.page.snack_bar = SnackBar(
            content=Text(
                "New contact saved",
            )
        )
        self.page.snack_bar.open = True
        self.page.update()

    def show_dialog(self) -> None:
        def close_modal(event: ControlEvent) -> None:
            dialog.open = False
            self.page.update()

        dialog = AlertDialog(
            modal=True,
            content=Text("Add some info to save as a contact."),
            actions=[
                TextButton(
                    text="Ok",
                    on_click=close_modal,
                )
            ]
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def on_name_changed(self, event: ControlEvent) -> None:
        name = event.control.value.strip()
        if name:
            initials = list(map(lambda x: x[0],name.split(" ")[:3]))
            self.ref_avatar_name_text.current.value = ''.join(initials)
        else:
            self.ref_avatar_name_text.current.value = "?"

        self.ref_avatar_name_text.current.update()

    def build(self):
        return Column(
            controls=[
                Container(
                    Stack(
                        controls=[
                            Container(
                                CircleAvatar(
                                    content=Text(
                                        "?",
                                        style=TextThemeStyle.DISPLAY_SMALL,
                                        ref=self.ref_avatar_name_text
                                    ),
                                    width=96,
                                    height=96,
                                ),
                                alignment=alignment.center,
                            )
                        ]
                    ),
                    margin=margin.only(right=16),
                ),
                Row(
                    controls=[
                        Icon(
                            icons.PERSON,
                            size=36,
                        ),
                        TextField(
                            label="Name",
                            on_change=self.on_name_changed,
                            expand=True,
                            ref=self.ref_name_field,
                        ),
                        TextField(
                            label="Last name",
                            expand=True,
                            ref=self.ref_last_name_field,
                        )
                    ]
                ),
                Row(
                    controls=[
                        Icon(
                            icons.EMAIL,
                            size=36,
                        ),
                        TextField(
                            label="Email",
                            expand=True,
                            ref=self.ref_email_field,
                        ),
                    ]
                ),
                Row(
                    controls=[
                        Icon(
                            icons.PHONE,
                            size=36,
                        ),
                        TextField(
                            label="Phone",
                            expand=True,
                            ref=self.ref_phone_field
                        )
                    ]
                )
            ]
        )
