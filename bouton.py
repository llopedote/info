from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class GridGameApp(App):
	def build(self):
		self.title = 'Grid Game'
		grid = GridLayout(rows=4, cols=5)
		for i in range(20):
			grid.add_widget(Button(text=str(i + 1)))
		return grid

# Lancement de l'interface graphique
GridGameApp().run()