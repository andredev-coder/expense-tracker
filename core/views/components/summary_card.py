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
        
        self.amount_text = Text(f'${self.amount}', size=22, color=ColorName.WHITE, weight=FontWeight.BOLD)
        self._content = Column()


    def set_amount(self, amount: float) -> None:
        self.amount_text.value = f'${amount}'
        self.amount = amount
        self.update()

    def build(self) -> None:
        self._content.controls = [
            Column(
                controls=[
                    Icon(name=self.icon_name, color=ColorName.WHITE),
                    Column(
                        controls=[
                            Text(self.title, size=14, color=ColorName.WHITE),
                            self.amount_text
                        ],
                        spacing=0
                    )
                ]
            )
        ]
        self.content = Container(content=self._content)

