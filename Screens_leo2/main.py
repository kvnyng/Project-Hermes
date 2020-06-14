# -*- coding: utf-8 -*-

from kivy.app import App
from kivymd.theming import ThemeManager
from kivy.uix.screenmanager import ScreenManager, Screen

class hermes(App):
    theme_cls = ThemeManager()


class WindowManager(ScreenManager):
    pass

if __name__ == "__main__":
    hermes().run()
