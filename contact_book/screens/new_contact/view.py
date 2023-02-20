from flet import AppBar, Page, Text, View


class NewContactView(View):
    page: Page

    def __init__(self, page: Page) -> None:
        super().__init__()
        self.page = page

        self.route = "/new-contact"
        self.controls = [
            AppBar(
                title=Text("New Contact"),
            ),
            Text("New Contact"),
        ]
