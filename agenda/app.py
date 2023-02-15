from flet import Page, app, Text

def main(page: Page) -> None:
    page.title = 'Agenda'
    page.add(
        Text(
            value="Hello, world!",
        )
    )

def run_app() -> None:
    app(
        name="Agenda",
        target=main,
    )
    