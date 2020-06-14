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
            text: "I'm not feeling well"
            on_release:
                app.root.ids.scr_mngr.current = "about"
                root.manager.transition.direction = "right"
        Button:
            text: "I think I'll be robbed"
            on_release:
                app.root.ids.scr_mngr.current = "about"
                root.manager.transition.direction = "right"
        Image:
            source: '/home/benitez/Desktop/Project-Hermes/Screens_leo2/data/assets/static_img.jpg'
        #Button:
        #    text: "Other problem"
        #    on_release:
        #        app.root.ids.scr_mngr.current = "about"
        #        root.manager.transition.direction = "right"
""")


class DashboardScreen(Screen):
    pass
