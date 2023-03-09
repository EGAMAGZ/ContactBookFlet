from flet import (
    KeyboardEvent,
    Page,
    RouteChangeEvent,
    TemplateRoute,
    ThemeMode,
    ViewPopEvent,
    app,
)

from contact_book.screens.contact_list.view import ContactListView
from contact_book.screens.new_contact.view import NewContactView
from contact_book.storage.settings import Settings
from contact_book.theme import THEME_DARK, THEME_LIGHT


class ContactBookApp:
    page: Page
    settings: Settings

    def __init__(self, page: Page) -> None:
        super().__init__()
        self.page = page
        self.settings = Settings(page)

    def initialize(self) -> None:
        self.page.padding = 0

        self.page.theme_mode = self.settings.get_theme_mode()
        self.page.on_keyboard_event = self.on_keyboard_event
        self.page.on_route_change = self.on_route_change
        self.page.on_view_pop = self.on_view_pop

        self.page.go("/")
        self.page.update()

    def on_route_change(self, event: RouteChangeEvent) -> None:
        self.page.views.clear()
        troute = TemplateRoute(self.page.route)
        # if troute.match('/'):
        self.page.views.append(
            ContactListView(self.page)
        )
        if troute.match('/new-contact'):
            self.page.views.append(
                NewContactView(self.page)
            )
        self.page.update()

    def on_view_pop(self, event: ViewPopEvent) -> None:
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)

    def on_keyboard_event(self, event: KeyboardEvent) -> None:
        if event.control and event.shift and event.key == "S":
            self.show_semantics_debugger()
        elif event.control and event.shift and event.key == "D":
            self.change_theme_mode()
        elif event.control and event.key=="N":
            self.page.go("/new-contact")

    # Show the semantics debugger
    def show_semantics_debugger(self) -> None:
        self.page.show_semantics_debugger = not self.page.show_semantics_debugger
        self.page.update()

    def change_theme_mode(self) -> None:
        self.settings.set_theme_mode(
            ThemeMode.DARK if self.page.theme_mode == ThemeMode.LIGHT
            else ThemeMode.LIGHT
        )
        self.page.theme_mode = self.settings.get_theme_mode()
        self.page.update()

def main(page: Page) -> None:
    page.title = 'Contact book'

    page.theme = THEME_LIGHT
    page.dark_theme = THEME_DARK

    agenda_app = ContactBookApp(page)
    agenda_app.initialize()

def run_app() -> None:
    app(
        name="Contact book",
        target=main,
    )
