from functools import partial

import pytermgui as ptg

from pytermgui import (
    WindowManager,
    Container,
    Splitter,
    Label,
    Button,
    Collapsible
)

from pytermgui.ansi_interface import MouseAction, MouseEvent
from pytermgui.enums import Overflow, HorizontalAlignment, VerticalAlignment
from pytermgui.input import keys
from pytermgui import styles as w_styles


class Window(ptg.Window):
    is_static = True
    # is_noresize = True
    is_persistent = True
    overflow = Overflow.SCROLL

    def __init__(self, *widgets, **attrs):
        if "box" not in attrs:
            attrs["box"] = "SINGLE"
        super().__init__(*widgets, **attrs)


class ClickableContainer(Container):
    def __init__(self, *widgets, **attrs):
        if "onclick" not in attrs:
            attrs["onclick"] = partial(print, "hello world")
        self.onclick = attrs["onclick"]
        super().__init__(*widgets, **attrs)

    def handle_mouse(self, event: MouseEvent) -> bool:
        if event.action == MouseAction.LEFT_CLICK:
            self.onclick()
            return True
        return False


class LineGap(Container):
    def __init__(self):
        super().__init__(" ", box="EMPTY")


class InputField(ptg.InputField):
    key_events = {}

    def set_key_events(self, key_events: dict[keys, partial]):
        self.key_events = key_events

    def handle_key(self, key: str) -> bool:
        for event in self.key_events:
            if key == event:
                self.key_events[event]()
                return True
        return super().handle_key(key)


with WindowManager() as manager:
    # setup
    Splitter.set_char("separator", " ")
    # define layouts
    manager.layout.add_slot("topbar", height=3, width=1.0)
    manager.layout.add_break()
    manager.layout.add_slot("sidebar", width=0.2)
    manager.layout.add_slot("body")
    manager.layout.add_break()
    manager.layout.add_slot("bottombar", height=3)

    # left body
    sidebar = Window()
    manager.add(sidebar, assign="sidebar")

    # body
    body = Window()
    manager.add(body, assign="body")

    def update_body(body, *widgets):
        body.set_widgets(widgets)
        manager.layout.apply()
        manager.compositor.redraw()
        body.focus()

    # home widget
    home = Container("Home")

    # explore widget
    explore = Container("Explore")

    # account widget
    username_input = InputField(prompt="Username: ")
    password_input = InputField(prompt="Password: ")
    on_submit_button_click = partial(print, "Submitted.")
    account = Container(
        LineGap(),
        username_input,
        LineGap(),
        password_input,
        LineGap(),
        Button("Login", onclick=on_submit_button_click),
        LineGap(),
        static_width=60,
        box="EMPTY_VERTICAL"
    )

    # bottombar
    on_home_click = partial(update_body, body, home)
    on_explore_click = partial(update_body, body, explore)
    on_account_click = partial(update_body, body, account)
    bottombar = Window(
        Splitter(
            ClickableContainer("Home", onclick=on_home_click),
            ClickableContainer("Explore", onclick=on_explore_click),
            ClickableContainer("Account", onclick=on_account_click),
        ),
        box="EMPTY"
    )
    manager.add(bottombar, assign="bottombar")

    # topbar
    status = "Best offers on mobile phones"
    title = "[bold skyblue]Flipkart [bold yellow] ([/] {} [bold yellow])[/]"
    topbar = Window(
        Splitter(
            Label(title.format(status),
                  parent_align=HorizontalAlignment.LEFT, box="EMPTY"),
            Button("Exit", onclick=lambda *_: manager.stop(),
                   parent_align=HorizontalAlignment.RIGHT)
        ),
        box="SINGLE"
    )
    manager.add(topbar, assign="topbar")
