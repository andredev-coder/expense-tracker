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
    AlertDialog,

    TextAlign,
    MainAxisAlignment,
    CrossAxisAlignment,
    TextButton,
    DismissibleDismissEvent,

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
from typing import Callable
from core.models import TransactionType



class TransactionList(Container):
    def __init__(self):
        super().__init__()

        # self.transactions = []
        self.list = ListView(
            controls=[],
            expand=True,
            spacing=10,
            auto_scroll=True
        )

        self.on_transaction_card_dismiss: Callable

        self._content = Column(
            controls=[
                Text('Transactions', size=18, weight=FontWeight.BOLD, color=ColorName.with_opacity(0.9, ColorName.BLACK)),
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

    def handle_dismiss(self, e: DismissibleDismissEvent):
        if e.control in self.list.controls:
            transaction_id = e.control.data
            self.on_transaction_card_dismiss(
                transaction_id
            )
            self.list.controls.remove(e.control)
            self.list.update()

    def add_transaction_card(self, id, type: TransactionType, subtitle, date, amount):
        if type == TransactionType.INCOME:
            icon = IconName.ATTACH_MONEY
            icon_color = ColorName.LIGHT_GREEN_ACCENT
        else:
            icon = IconName.MONEY_OFF_SHARP
            icon_color = ColorName.RED_500

        self.list.controls.append(
            self.transaction_card(id, icon, icon_color, type.title(), subtitle, date, amount)
        )
        self.list.update()

    def transaction_card(self, id, icon: IconName, icon_color: ColorName, title, subtitle, date, amount) -> Dismissible:
        return Dismissible(
            content=Container(
                bgcolor=ColorName.WHITE,
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
                                Icon(name=icon, color=icon_color),
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
            ),
            dismiss_direction=DismissDirection.END_TO_START,
            on_dismiss=self.handle_dismiss,
            dismiss_thresholds={
                DismissDirection.HORIZONTAL: 0.1,
                DismissDirection.START_TO_END: 0.1,
            },
            data=id
        )

