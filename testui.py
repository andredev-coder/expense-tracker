import flet         # type: ignore
from flet import (  # type: ignore
    Page,
    Container,
    Column,
    Row,
    Text,
    TextField,
    ElevatedButton,
    IconButton,
    DataTable,
    DataColumn,
    DataRow,
    DataCell,
    ListView,
    ListTile,
    Dismissible,
    DismissDirection,
    ControlState,
    BorderSide,
    RoundedRectangleBorder,
    ScrollbarTheme,

    ControlEvent,
    ScrollMode,

    TextAlign,
    MainAxisAlignment,
    CrossAxisAlignment,

    Offset,
    BoxShadow,
    Theme,
    TextStyle,
    ButtonStyle,
    FontWeight,
    Icon,

    border,
    border_radius,
    padding,
    margin
)
from flet import Colors as ColorName
from flet import Icons as IconName 




class SummaryCard(Container):
    def __init__(
        self, 
        title: str, 
        amount: float,
        icon_name: IconName, 
        color: ColorName
    ):
        super().__init__(
            width=150,
            height=100,
            border_radius=8,
            padding=10,
            bgcolor=color,
            border=border.all(width=1, color=ColorName.with_opacity(0.2, ColorName.BLACK))
        )
        self.title = title
        self.icon_name = icon_name
        self.amount = amount
        
        self._content = Column()


    def build(self) -> None:
        self._content.controls = [
            Column(
                controls=[
                    Icon(name=self.icon_name, color=ColorName.WHITE),
                    Column(
                        controls=[
                            Text(self.title, size=14, color=ColorName.WHITE),
                            Text(f'${self.amount}', size=22, color=ColorName.WHITE, weight=FontWeight.BOLD)
                        ],
                        spacing=0
                    )
                ]
            )
        ]
        self.content = Container(content=self._content)


# class ExpenseCard(SummaryCard):
#     def __init__(self, title: str, amount: float):
#         super().__init__(
#             title,
#             amount,
#             IconName.WALLET_OUTLINED,
#             ColorName.BLUE
#         )

# class IncomeCard(SummaryCard):
#     def __init__(self, title: str, amount: float):
#         super().__init__(
#             title,
#             amount,
#             IconName.MONETIZATION_ON,
#             ColorName.PINK
#         )





class AddTransactionForm(Container):
    def __init__(self):
        super().__init__()

        self._content = Column(spacing=20)

    def build(self) -> None:
        self._content.controls = [
            Column(
                controls=[
                    Column(
                        controls=[
                            Text(
                                value='Description', 
                                color=ColorName.with_opacity(0.9, ColorName.BLACK),
                                size=16, 
                                weight=FontWeight.BOLD
                            ),
                            TextField(
                                hint_text='Please enter description',
                                border_radius=8,
                                border_color=ColorName.with_opacity(0.2, ColorName.BLACK),
                                hint_style=TextStyle(color=ColorName.with_opacity(0.8, ColorName.BLACK)),
                                text_style=TextStyle(color=ColorName.BLACK)

                            )
                        ],
                        spacing=0
                    ),
                    Column(
                        controls=[
                            Text(
                                value='Amount (negative - expense, positive - income)',
                                color=ColorName.with_opacity(0.9, ColorName.BLACK),
                                weight=FontWeight.BOLD,
                                size=16, 
                            ),
                            TextField(
                                hint_text='Please enter amount',
                                border_radius=8,
                                border_color=ColorName.with_opacity(0.2, ColorName.BLACK),
                                hint_style=TextStyle(color=ColorName.with_opacity(0.8, ColorName.BLACK)),
                                text_style=TextStyle(color=ColorName.BLACK)
                            )
                        ],
                        spacing=0
                    )
                ]
            ),
            ElevatedButton(
                text='Add Transaction',
                height=40,
                width=140,
                color=ColorName.WHITE,
                style=ButtonStyle(
                    shape=RoundedRectangleBorder(radius=border_radius.all(8)),  # скругление 15px
                    bgcolor=ColorName.DEEP_PURPLE_500  
                )
            )
        ]
        self.content = Container(content=self._content)


class TransactionList(Container):
    def __init__(self):
        super().__init__()

        self.transactions = [
            Dismissible(
                content=self.transaction_card(
                    icon=IconName.CATEGORY,
                    icon_color=ColorName.AMBER,
                    title="Test 1",
                    subtitle="Products",
                    date="2022-10-11",
                    amount="-$500.00"
                ),
                dismiss_direction=DismissDirection.HORIZONTAL,
                on_dismiss=self.handle_dismiss,
                dismiss_thresholds={
                    DismissDirection.HORIZONTAL: 0.1,
                    DismissDirection.START_TO_END: 0.1,
                },
            )
            for _ in range(6)
        ]
        self.list = ListView(
            controls=self.transactions,
            expand=True,
            spacing=10,
            auto_scroll=True
        )

        self._content = Column(
            controls=[
                Text('Transactions', size=16, weight=FontWeight.BOLD, color=ColorName.with_opacity(0.9, ColorName.BLACK)),
                Container(
                    content=self.list,
                    padding=padding.symmetric(vertical=10),
                    border=border.all(2, ColorName.GREY_300),
                    border_radius=8,
                    height=255,
                    bgcolor=ColorName.with_opacity(0.05, ColorName.BLACK)
                )
            ],
            expand=True
        )

    def build(self) -> None:
        self.content = Container(content=self._content)

    def handle_dismiss(self, e: ControlEvent):
        self.transactions.remove(e.control)
        self.list.controls.remove(e.control)
        self.list.update()

    @staticmethod
    def transaction_card(icon, icon_color, title, subtitle, date, amount) -> Container:
        return Container(
            bgcolor=ColorName.WHITE,
            # border=border.all(1, color=ColorName.with_opacity(0.2, ColorName.BLACK)),
            border_radius=8,
            shadow=BoxShadow(
                blur_radius=8,
                spread_radius=1,
                color=ColorName.with_opacity(0.1, ColorName.BLACK),
                offset=Offset(4, 4)  
            ),
            height=70,
            expand=True,
            margin=margin.symmetric(horizontal=10),
            padding=padding.symmetric(horizontal=10),
            content=Row(
                controls=[
                    Row(
                        controls=[
                            Icon(name=IconName.ADD_TASK_SHARP, color=ColorName.DEEP_PURPLE_500),
                            Column(
                                controls=[
                                    Text(title, color=ColorName.with_opacity(0.9, ColorName.BLACK)),
                                    Text(subtitle, size=12, color=ColorName.with_opacity(0.9, ColorName.BLACK)),
                                    Text(date, size=10, color=ColorName.with_opacity(0.9, ColorName.BLACK))
                                ],
                                spacing=0,
                                alignment=MainAxisAlignment.CENTER
                            )
                        ]
                    ),
                    Text(amount, color=ColorName.with_opacity(0.9, ColorName.BLACK))
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN
            )
        )




def main(page: Page):
    page.fonts = {
        'Overpass': 'https://github.com/RedHatOfficial/Overpass/blob/master/fonts/ttf/Overpass-Bold.ttf'
    }
    page.theme = Theme(font_family="Overpass", scrollbar_theme=ScrollbarTheme(thickness=0))

    page.window.min_width = 545
    page.window.width = 545
    page.window.max_height = 750
    page.window.min_height = 750
    page.window.height = 750

    page.add(
        Container(
            content=Column(
                controls=[
                    Container(
                        content=Row(
                            controls=[
                                SummaryCard('Balance', 100, IconName.ACCOUNT_BALANCE, ColorName.ORANGE),
                                SummaryCard('Expenses', 100, IconName.WALLET_OUTLINED, ColorName.BLUE),
                                SummaryCard('Income', 100, IconName.MONETIZATION_ON, ColorName.PINK),
                            ]
                        )
                    ),
                    AddTransactionForm(),
                    TransactionList()
                ],
                spacing=20
            ),
            padding=padding.all(20),
            bgcolor=ColorName.WHITE,
        )
    )
    page.update()


flet.app(target=main)