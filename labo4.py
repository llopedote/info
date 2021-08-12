from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

# 1
class Fahrenheit(App):
	def build(self):
		root = BoxLayout(orientation="vertical")
		line1 = BoxLayout(orientation="horizontal")
		line2 = BoxLayout(orientation="horizontal")

		# Par défaut, le size_hint vaut (1, 1) c-à-d 1 dans le sens horizontal et
		# 1 dans le sens vertical. Ici on utilise un size_hint de (2, 1), on a
		# donc des TextInput qui seront 2 fois plus larges que les autres éléments du
		# même BoxLayout
		self.__inputCelcius = TextInput(size_hint=(2, 1))
		self.__inputFahrenheit = TextInput(size_hint=(2, 1))

		self.__buttonC2F = Button(text="v")
		self.__buttonC2F.bind(on_press=self.cel2fah)
		self.__buttonF2C = Button(text="^")
		self.__buttonF2C.bind(on_press=self.fah2cel)

		line1.add_widget(Label(text="Celcius"))
		line1.add_widget(self.__inputCelcius)
		line1.add_widget(self.__buttonC2F)

		line2.add_widget(Label(text="Fahrenheit"))
		line2.add_widget(self.__inputFahrenheit)
		line2.add_widget(self.__buttonF2C)

		root.add_widget(line1)
		root.add_widget(line2)

		return root

	def cel2fah(self, source):
		try:
			celcius = float(self.__inputCelcius.text)
			self.__inputFahrenheit.text = str(9*celcius/5+32)
		except ValueError:
			self.__inputCelcius.text = "Entrée invalide"

	def fah2cel(self, source):
		try:
			fahrenheit = float(self.__inputFahrenheit.text)
			self.__inputCelcius.text = str((fahrenheit - 32)*5/9)
		except ValueError:
			self.__inputFahrenheit.text = "Entrée invalide"

# 2
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

#Fahrenheit().run()
Clavier().run()
