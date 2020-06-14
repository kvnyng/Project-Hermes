from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string("""
<DashboardScreen>
    name: 'dashboard'
    ScrollView:
        id: scroll
        do_scroll_x: False
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(800)
            padding: dp(15)
            spacing: dp(15)
            MDLabel:
                font_style: 'Body1'
                theme_text_color: 'Secondary'
                text: 'There is no need'#ut.get_data('texts2')['dashboard']
""")


class DashboardScreen(Screen):
    pass
