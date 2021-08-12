import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout

class FenetreApp(App):
 
    def build(self):
        Fenetre = BoxLayout()
        #importe images  avec etirement
        self.Imagejeux=Image(source='master.png',allow_stretch=True,keep_ratio=False)

        self.Fenetre.add_widget(self.Imagejeux)
       
        #On cree un bouton:
        box = BoxLayout()
        self.Boutonplay=Button(text='Play',size_hint=(0.3, 0.1))
        self.Boutonplay.pos_hint={'right': 0.65,}
        self.Boutonplay.bind(on_press=self.une_fonction_bouton)
       
        #On ajoute l'image et le bouton dans le box:
        box.add_widget(self.Boutonplay)
       
        #On affiche la racine:
        return Fenetre and Boutonplay
 
    def une_fonction_bouton(self,instance):#Pour le bouton
        print("coucou")
 
if __name__ == '__main__':
    FenetreApp().run()