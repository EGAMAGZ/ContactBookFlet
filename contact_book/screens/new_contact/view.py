from flet import Page, View

from contact_book.screens.new_contact.screen import NewContactScreen


class NewContactView(View):
    page: Page

    def __init__(self, page: Page) -> None:
        super().__init__()
        self.page = page

        self.route = "/new-contact"
        self.controls = [
            NewContactScreen(
                page=self.page,
                parent_view=self,
            )
        ]
