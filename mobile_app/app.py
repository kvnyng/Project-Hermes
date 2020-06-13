import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.popup import Popup

class MainWindow(Screen):
    userName = 'Leonardo'
    def callPolice(self):
        print(self.userName, '- fuck the police')

    def popup(self):
        show = MyPopup()
        popupWindow = Popup(title="More information", content=show,
                            size_hint=(None, None), size=(400, 400))
        popupWindow.open()


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MyPopup(Screen):
    pass

kv = Builder.load_file("design.kv")
class MyMainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()
