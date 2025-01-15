"""
Usage: Creates families of related objects without specifying their concrete classes.
"""

from fastapi import FastAPI


class Button:
    def render(self):
        pass


class WindowsButton(Button):
    def render(self):  # type: ignore
        return "Rendered Windows Button"


class MacButton(Button):
    def render(self):  # type: ignore
        return "Rendered Mac Button"


class UIFactory:
    def create_button(self) -> Button:  # type: ignore
        pass


class WindowsUIFactory(UIFactory):
    def create_button(self) -> Button:
        return WindowsButton()


class MacUIFactory(UIFactory):
    def create_button(self) -> Button:
        return MacButton()


app = FastAPI()


def get_ui_factory(os_type: str) -> UIFactory:
    if os_type == "windows":
        return WindowsUIFactory()
    elif os_type == "mac":
        return MacUIFactory()
    return None  # type: ignore


@app.get("/ui")
async def get_ui(os_type: str = "windows"):
    factory = get_ui_factory(os_type)
    button = factory.create_button()
    return {"button": button.render()}
