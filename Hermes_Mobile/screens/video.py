import kivy

from kivy.app import App
from kivy.lang import Builder

root = Builder.load_string('''
VideoPlayer:
    source: 'https://vimeo.com/192521116'
''')

class TestApp(App):
    def build(self):
        return root

if __name__ == '__main__':
    TestApp().run()
