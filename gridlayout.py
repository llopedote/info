from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage


#Fenetre de depart avec images
class MyGridLayout(GridLayout):
    def __init__(self,**kwargs):
        super(MyGridLayout,self).__init__(**kwargs)
        self.rows=2

        self.topgrid = GridLayout()
        self.topgrid.cols = 2



        self.topgrid.add_widget(Button(text="Name:",
        font_size = 32,
        size_hint_y=0.1,
        height=50,
        size_hint_x = 0.5,
        width = 200))
        self.name = TextInput(multiline=False)
        self.topgrid.add_widget(self.name)


        self.topgrid.add_widget(AsyncImage(source = 'images/master.png'))

        self.topgrid.add_widget(AsyncImage(source = 'images/master.png'))


        self.add_widget(self.topgrid)

        self.submit = Button(text = 'Play the Game',
        font_size = 32,
        size_hint_y=None,
        height=50,
        size_hint_x = 0.5,
        width = 200)
        

        self.submit.bind(on_press = self.press)
        self.add_widget(self.submit)

    def press(self,instance):
        name = self.name.text
            
        self.add_widget(Label(text=f" User : {name} Enjoy The Game !"))

class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (0,0,0.35,1)
        return MyGridLayout()


#passage sur l ecran de jeu


if __name__ == "__main__":
    AwesomeApp().run()