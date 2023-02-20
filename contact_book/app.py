from flet import (
    KeyboardEvent,
    Page,
    RouteChangeEvent,
    TemplateRoute,
    ThemeMode,
    app,
)

from contact_book.screens.contact_list.view import ContactListView
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

        self.page.go("/")
        self.page.update()

    def on_route_change(self, event: RouteChangeEvent) -> None:
        self.page.views.clear()
        troute = TemplateRoute(self.page.route) # noqa: F841
        if troute.match('/'):
            self.page.views.append(
                ContactListView(self.page)
            )
        self.page.update()

    def on_view_pop(self, view) -> None:
        print(type(view))
        pass

    def on_keyboard_event(self, event: KeyboardEvent) -> None:
        if event.control and event.shift and event.key == "S":
            self.page.show_semantics_debugger = not self.page.show_semantics_debugger
            self.page.update()
        elif event.control and event.shift and event.key == "D":
            self.change_theme_mode()

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
