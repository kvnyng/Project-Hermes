from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image, AsyncImage

Builder.load_string("""
<DashboardScreen>
    name: 'dashboard'
    GridLayout:
        cols:1
        size: root.width, root.height

        Button:
            text: "Chamar um médico"
            font_size: 30
            on_release:
                app.root.ids.scr_mngr.current = "about"
                root.manager.transition.direction = "right"
        Button:
            text: "Chamar a polícia"
            font_size: 30
            on_release:
                app.root.ids.scr_mngr.current = "about"
                root.manager.transition.direction = "right"
        Button:
            text: "Chamar a família"
            font_size: 30
            on_release:
                app.root.ids.scr_mngr.current = "about"
                root.manager.transition.direction = "right"
        Button:
            text: "Voltar"
            font_size: 30
            on_release:
                app.root.ids.scr_mngr.current = "about"
                root.manager.transition.direction = "right"
""")


class DashboardScreen(Screen):
    pass
