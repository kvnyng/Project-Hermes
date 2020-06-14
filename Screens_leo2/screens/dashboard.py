from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

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
        Button:
            text: "Other problem"
            on_release:
                app.root.ids.scr_mngr.current = "about"
                root.manager.transition.direction = "right"
""")


class DashboardScreen(Screen):
    pass
