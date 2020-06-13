# -*- coding: utf-8 -*-

from kivy.app import App
from kivymd.theming import ThemeManager


class hermes(App):
    theme_cls = ThemeManager()


if __name__ == "__main__":
    hermes().run()
