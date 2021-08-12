from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout




class Clavier(App):
	def build(self):
		keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "0", "<<"]
		grid = GridLayout(cols=3, size_hint=(1, 4))
		for key in keys:
				button = Button(text=key)
				if key == ".":
					button.bind(on_press=self.point)
				elif key == "<<":
					button.bind(on_press=self.back)
				else:
					button.bind(on_press=self.digit)
				grid.add_widget(button)

		self.__screen = Label()
		root = BoxLayout(orientation='vertical')
		root.add_widget(self.__screen)
		root.add_widget(grid)
		return root

	def digit(self, source):
		self.__screen.text += source.text

	def point(self, source):
		if '.' not in self.__screen.text:
			self.__screen.text += '.'

	def back(self, source):
		if len(self.__screen.text) > 0:
			self.__screen.text = self.__screen.text[:-1]

Clavier().run()