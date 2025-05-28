
from kivy.app import App
from kivy.uix.label import Label

class PannelloApp(App):
    def build(self):
        return Label(text="Ciao dal pannello!")

if __name__ == '__main__':
    PannelloApp().run()
