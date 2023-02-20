from flet import Page, View

from contact_book.screens.contact_list.screen import ContactListScreen


class ContactListView(View):
    def __init__(self, page: Page):
        super().__init__()
        self.route = "/"

        self.controls = [
            ContactListScreen(page),
        ]
