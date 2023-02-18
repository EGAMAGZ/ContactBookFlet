from flet import (
    Column,
    Container,
    IconButton,
    MainAxisAlignment,
    Row,
    Text,
    TextField,
    TextThemeStyle,
    UserControl,
    border_radius,
    colors,
    icons,
    padding,
    InputBorder,
)


class ContactListScreen(UserControl):
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
            ]
        )
