from kivy.app import App
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class SpinnerExample(App):
	def build(self):
		box = BoxLayout(orientation="vertical")
		line = BoxLayout(orientation="horizontal")
		self.__spinner = Spinner(text="", values=["un garçon", "une fille", "un robot"])
		button = Button(text="OK")
		self.__output = Label()

		line.add_widget(self.__spinner)
		line.add_widget(button)

		box.add_widget(line)
		box.add_widget(self.__output)

		button.bind(on_press=self.action)

		return box

	def action(self, source):
		self.__output.text = "Je suis {}".format(self.__spinner.text)

SpinnerExample().run()