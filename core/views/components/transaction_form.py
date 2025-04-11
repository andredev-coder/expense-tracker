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
from typing import Callable, Optional


type Callback = Callable[[float, str], None]


class TransactionForm(Container):
    def __init__(self):
        super().__init__()

        self.callback: Callback

        self.description_field = TextField(
            hint_text='Please enter description',
            border_radius=8,
            border_color=ColorName.with_opacity(0.2, ColorName.BLACK),
            hint_style=TextStyle(color=ColorName.with_opacity(0.8, ColorName.BLACK)),
            text_style=TextStyle(color=ColorName.BLACK)
        )
        self.amount_field = TextField(
            hint_text='Please enter amount',
            border_radius=8,
            border_color=ColorName.with_opacity(0.2, ColorName.BLACK),
            hint_style=TextStyle(color=ColorName.with_opacity(0.8, ColorName.BLACK)),
            text_style=TextStyle(color=ColorName.BLACK)
        )
        self.add_transaction_button = ElevatedButton(
            text='Add Transaction',
            height=40,
            width=140,
            color=ColorName.WHITE,
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=border_radius.all(8)),  
                bgcolor=ColorName.DEEP_PURPLE_500  
            ),
            on_click=self.on_add_transaction
        )

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
                            self.description_field
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
                            self.amount_field
                        ],
                        spacing=0
                    )
                ]
            ),
            self.add_transaction_button
        ]
        self.content = Container(content=self._content)


    def on_add_transaction(self, event: ControlEvent) -> None:
        try:                
            self.callback(
                float(self.amount_field.value),
                self.description_field.value
            )   

            self.description_field.value = ''
            self.amount_field.value = ''
            self.update()
        except ValueError:
            return
        


