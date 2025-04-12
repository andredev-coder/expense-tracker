from flet import ( # type: ignore
    Page,
    Container, 
    ThemeMode,
    ScrollMode,
    CrossAxisAlignment,
    MainAxisAlignment,
    Column,
    ScrollbarTheme,
    Theme,
    Row,
    Text, 
    FontWeight, 
    VerticalDivider,
    padding
) 
from .components import SummaryCard, TransactionForm, TransactionList

from flet import Colors as ColorName
from flet import Icons as IconName 







class ApplicationView():
    def __init__(self, page: Page):
        self.page = page
        self.page.title = 'Financial Tracker'
        page.theme_mode = ThemeMode.LIGHT
        page.horizontal_alignment = CrossAxisAlignment.START
        page.vertical_alignment = MainAxisAlignment.START
        page.padding = 0

        page.window.min_width = 545
        page.window.width = 545
        page.window.max_height = 750
        page.window.min_height = 750
        page.window.height = 750

        self.transaction_form = TransactionForm()
        self.transaction_list = TransactionList()
        self.expense_card = SummaryCard('Expenses', 0, IconName.WALLET_OUTLINED, ColorName.BLUE)
        self.income_card = SummaryCard('Income', 0, IconName.MONETIZATION_ON, ColorName.PINK)

        page.fonts = {
            'Overpass': 'https://github.com/RedHatOfficial/Overpass/blob/master/fonts/ttf/Overpass-Bold.ttf'
        }
        page.theme = Theme(font_family="Overpass", scrollbar_theme=ScrollbarTheme(thickness=0))


        self.balance = Text(
            value='$0.0', 
            color=ColorName.with_opacity(0.9, ColorName.BLACK),
            size=24, 
            weight=FontWeight.BOLD
        )

        page.add(
            Container(
                content=Column(
                    controls=[
                        Column(
                            controls=[
                                Text(
                                    value='Your Balance', 
                                    color=ColorName.with_opacity(0.9, ColorName.BLACK),
                                    size=24, 
                                    weight=FontWeight.BOLD
                                ),
                                self.balance
                            ],
                            spacing=0
                        ),
                        Container(
                            content=Row(
                                controls=[
                                    self.expense_card,
                                    self.income_card,
                                ]
                            )
                        ),
                        self.transaction_form,
                        self.transaction_list
                    ],
                    spacing=20
                ),
                padding=padding.all(20),
                bgcolor=ColorName.WHITE,
            )
        )
        page.update()