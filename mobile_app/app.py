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
'''
class MyGrid(Widget):


class MyApp(App):  # <- Main Class
    def build(self):
        grid = MyGrid()
        grid.userName = "Leonardo"
        return grid

if __name__ == "__main__":
    MyApp().run()
'''

class MainWindow(Screen):
    userName = 'Leonardo'
    def pressed(self):
        print(self.userName, '- fuck the police')


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("design.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
