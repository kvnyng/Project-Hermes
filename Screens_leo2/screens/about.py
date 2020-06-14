from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string("""
<AboutScreen>
    name: 'about'
    GridLayout:
        cols:1
        GridLayout:
            orientation: 'vertical'
            size_hint_y: None
            cols: 2
            MDLabel:
                text: 'fuck Trump1'#ut.get_data('texts')['about']

            MDLabel:
                text: 'fuck Trump2'#ut.get_data('texts')['about']

            MDLabel:
                text: 'fuck Trump3'#ut.get_data('texts')['about']
            MDLabel:
                text: 'fuck Trump3'#ut.get_data('texts')['about']
        Button:
            text:"Call the police"
            on_release:
                print('fuck the police')
                app.root.ids.scr_mngr.current = 'dashboard'
                #app.root.current = "about"
                #root.manager.transition.direction = "left"
""")


class AboutScreen(Screen):
    pass
