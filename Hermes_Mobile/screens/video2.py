from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer


class TestApp(App):
    vid = None

    def replay(self, instance, value):
        if value != "play":
            # self.vid.play = True
            self.vid.state = "play"

    def build(self):
        self.vid = VideoPlayer(source="/Users/btluu/Downloads/Project-Hermes-master/Screens_leo2/data/assets/pixar.mp4", state="play")
        # self.vid.bind(state=self.replay)  # When state changes, if not playing, play it
        return self.vid


TestApp().run()
