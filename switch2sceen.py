from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen

class ScreenManagerExample(App):
	def build(self):
		self.__manager = ScreenManager()
		self.__manager.add_widget(self.buildScreen1())
		self.__manager.add_widget(self.buildScreen2())
		return self.manager

	def buildScreen1(self):
		screen = Screen(name="screen1")
		box = BoxLayout(orientation="vertical")
		box.add_widget(Label(text="Screen 1"))
		button = Button(text="Go to Screen 2")
		button.bind(on_press=self.toScreen2)
		screen.add_widget(box)
		box.add_widget(button)
		return screen

	def buildScreen2(self):
		screen = Screen(name="screen2")
		box = BoxLayout(orientation="vertical")
		box.add_widget(Label(text="Screen 2"))
		button = Button(text="Go to Screen 1")
		button.bind(on_press=self.toScreen1)
		screen.add_widget(box)
		box.add_widget(button)
		return screen

	def toScreen2(self, source):
		# Use the name of the destination Screen
		self.__manager.current = "screen2"

	def toScreen1(self, source):
		self.__manager.current = "screen1"

ScreenManagerExample().run()