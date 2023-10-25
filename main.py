from kivy.app import App
from kivy.app import Widget
from kivy.properties import ObjectProperty

class MygameApp(App):
    pass
class Background(Widget):
    floating_ground_texture = ObjectProperty(None)
    pass

MygameApp().run()
