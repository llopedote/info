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
from kivy.uix.screenmanager import ScreenManager, Screen

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
        height=70,
        size_hint_x = 0.5,
        width = 250))
        self.name = TextInput(multiline=False)
        self.topgrid.add_widget(self.name)


        self.topgrid.add_widget(AsyncImage(source = 'images/master.png'))

        self.topgrid.add_widget(AsyncImage(source = 'images/master.png'))


        self.add_widget(self.topgrid)

        self.submit = Button(text = 'Play the Game',
        font_size = 32,
        size_hint_y=None,
        height=70,
        size_hint_x = 0.5,
        width = 250)
        

        self.submit.bind(on_press = self.press)
        self.add_widget(self.submit)

    def press(self,instance):
        name = self.name.text
            
        self.add_widget(Label(text=f" User : {name} Enjoy The Game !"))

        giolala.info_page.update_info(name)
        giolala.screen_manager.current = 'Info'

class Manager(App):
    def build(self):
        self.screen_manager = ScreenManager()
        self.mygridlayout = MyGridLayout()
        screen = Screen(name='gridlayout')
        screen.add_widget(self.mygridlayout)
        self.screen_manager.add_widget(screen)

        self.info_page = InfoPage()
        screen = Screen(name='Info')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager
class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1

        self.message = Label(halign="center", valign="middle", font_size=30)

        self.message.bind(width=self.update_text_width)

        self.add_widget(self.message)


    def update_info(self, message):
        self.message.text = message
    def update_text_width(self, *_):
        self.message.text_size = (self.message.width * 0.9, None)

class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (0,0,0.35,1)
        return MyGridLayout()


#passage sur l ecran de jeu


if __name__ == "__main__":
    giolala = Manager()
    giolala.run()


