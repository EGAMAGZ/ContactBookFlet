from typing import overload
from flet import Page, ThemeMode

class Settings:
    page: Page

    def __init__(self, page: Page) -> None:
        self.page = page

    @overload
    def set_theme_mode(self, theme_mode: str) -> None:
        ...

    @overload
    def set_theme_mode(self, theme_mode: ThemeMode) -> None:
        ...

    def set_theme_mode(self, theme_mode):
        if isinstance(theme_mode, ThemeMode):
            self.page.client_storage.set("THEME_MODE", theme_mode.value)
        else:
            self.page.client_storage.set("THEME_MODE", theme_mode)

    def get_theme_mode(self) -> ThemeMode:
        if not self.page.client_storage.contains_key("THEME_MODE"):
            self.page.client_storage.set("THEME_MODE", ThemeMode.LIGHT.value)
        return ThemeMode(self.page.client_storage.get("THEME_MODE"))
