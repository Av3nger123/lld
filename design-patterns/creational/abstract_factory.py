from abc import ABC, abstractmethod


# Products
class Button:
    def render(self):
        return "Generic Button"
    
class Checkbox:
    def render(self):
        return "Generic Checkbox"

# Abstract Factory
class GUIFactory(ABC):
    
    @abstractmethod
    def create_button():
        pass
    
    @abstractmethod
    def create_checkbox():
        pass
    
# Windows variant of Products (Concrete Products)
class WindowsButton(Button):
    def render(self):
        return "Windows Button"
    
class WindowsCheckbox(Checkbox):
    def render(self):
        return "Windows Checkbox"
    
# Windows variant of Factory (Concrete Factory)
class WindowsFactory(GUIFactory):
    
    def create_button(self):
        return WindowsButton()
    
    def create_checkbox(self):
        return WindowsCheckbox()

# Mac variants of Products (Concrete Product)
class MacButton(Button):
    def render(self):
        return "Mac Button"
    
class MacCheckbox(Checkbox):
    def render(self):
        return "Mac Checkbox"
    
# Mac variant of Factory (Concrete Factory)
class MacFactory(GUIFactory):
    
    def create_button(self):
        return MacButton()
    
    def create_checkbox(self):
        return MacCheckbox()
    
class Client:
    
    factory: GUIFactory
    button: Button
    checkbox: Checkbox
    
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()
    
    def render(self):
        print(self.button.render() )
        print(self.checkbox.render()) 

config_map = {
    "win":WindowsFactory(),
    "mac":MacFactory()
}
if __name__ == "__main__":
    os_config = "win"
    factory = config_map.get(os_config)
    client = Client(factory)
    client.render()