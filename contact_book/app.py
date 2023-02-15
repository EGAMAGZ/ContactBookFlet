from flet import KeyboardEvent, Page, Text, UserControl, app, ThemeMode

from contact_book.storage.preferences.settings import Settings

class ContactBookApp(UserControl):
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

        self.page.update()

    def build(self):
        return Text(
            value="Hello world",
        )
    
    def on_keyboard_event(self, event: KeyboardEvent) -> None:
        if event.control and event.shift and event.key == "S":
            self.page.show_semantics_debugger = not self.page.show_semantics_debugger
            self.page.update()
        elif event.control and event.key == "D":
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
    
    agenda_app = ContactBookApp(page)
    page.add(agenda_app)
    agenda_app.initialize()

def run_app() -> None:
    app(
        name="Contact book",
        target=main,
    )
