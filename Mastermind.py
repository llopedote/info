import json
import sys

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
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.spinner import Spinner
from kivy.uix.image import AsyncImage
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color
from random import choices
from copy import deepcopy
from kivy.base import runTouchApp
from functools import partial
from kivy.uix.anchorlayout import AnchorLayout

#Fenetre de depart avec images
class MastermindApp(App):
    def build(self):
        self.titre = 'MasterMind'
        self.manager = ScreenManager()
        self.manager.add_widget(self.ScreenMenu())
        self.manager.add_widget(self.ScreenGame())
        self.manager.add_widget(self.ScreenVictory())
        self.manager.add_widget(self.ScreenDefeat())
        return self.manager
#ecran de jeu

    def ScreenGame(self):
        screen= Screen(name ="Game")
        self.box = BoxLayout(orientation ="vertical")
        self.tours = 1
        self.output_ratio = Label()
        self.output_ratio.text = self.winrate_ratio()

#initialisation des variables 28 output et 7 variable et couleurs

        self.output1 = Button(background_color = [0,0,0,0])
        self.output2 = Button(background_color = [0,0,0,0])
        self.output3 = Button(background_color = [0,0,0,0])
        self.output4 = Button(background_color = [0,0,0,0])
        self.output_valide1 = Label()
        self.output_color1 = Label ()


        self.output5 = Button(background_color = [0,0,0,0])
        self.output6 = Button(background_color = [0,0,0,0])
        self.output7 = Button(background_color = [0,0,0,0])
        self.output8 = Button(background_color = [0,0,0,0])
        self.output_valide2 = Label()
        self.output_color2 = Label ()

        self.output9 = Button(background_color= [0,0,0,0])
        self.output10 = Button(background_color = [0,0,0,0])
        self.output11 = Button(background_color = [0,0,0,0])
        self.output12 = Button(background_color = [0,0,0,0])
        self.output_valide3 = Label()
        self.output_color3 = Label ()

        self.output13 = Button(background_color = [0,0,0,0])
        self.output14 = Button(background_color = [0,0,0,0])
        self.output15 = Button(background_color = [0,0,0,0])
        self.output16 = Button(background_color = [0,0,0,0])
        self.output_valide4 = Label()
        self.output_color4 = Label ()


        self.output17 = Button(background_color = [0,0,0,0])
        self.output18 = Button(background_color = [0,0,0,0])
        self.output19 = Button(background_color = [0,0,0,0])
        self.output20 = Button(background_color = [0,0,0,0])
        self.output_valide5 = Label()
        self.output_color5 = Label ()

        self.output21 = Button(background_color = [0,0,0,0])
        self.output22 = Button(background_color = [0,0,0,0])
        self.output23 = Button(background_color = [0,0,0,0])
        self.output24 = Button(background_color = [0,0,0,0])
        self.output_valide6 = Label()
        self.output_color6 = Label ()


        self.output25 = Button(background_color = [0,0,0,0])
        self.output26 = Button(background_color = [0,0,0,0])
        self.output27 = Button(background_color = [0,0,0,0])
        self.output28 = Button(background_color = [0,0,0,0])
        self.output_valide7 = Label()
        self.output_color7 = Label ()


#def de la fenetre avec les inputs

        self.line1 = BoxLayout(orientation='horizontal')
        self.line1.add_widget(Label(text='User'))
        self.input1 = TextInput(multiline= False)
        self.line1.add_widget(self.input1)
        self.line1.add_widget(Label(text='Meilleur Resultat'))
        self.line1.add_widget(self.output_ratio)
        self.box.add_widget(self.line1)

        self.line2 = BoxLayout(orientation = 'horizontal')
        self.line2.add_widget(Label(text = 'Proposition', size_hint=(2/3,1)))
        self.line2.add_widget(Label(text = "Bonnes couleurs",size_hint =(1/6,1)))
        self.line2.add_widget(Label(text = 'Bons emplacements',size_hint = (1/6,1)))
        self.box.add_widget(self.line2)

        self.line3 = BoxLayout(orientation = 'horizontal')
        self.line3.add_widget(self.output1)
        self.line3.add_widget(self.output2)
        self.line3.add_widget(self.output3)
        self.line3.add_widget(self.output4)
        self.line3.add_widget(self.output_valide1)
        self.line3.add_widget(self.output_color1)
        self.box.add_widget(self.line3)

        self.line4 = BoxLayout(orientation = 'horizontal')
        self.line3.add_widget(self.output5)
        self.line3.add_widget(self.output6)
        self.line3.add_widget(self.output7)
        self.line3.add_widget(self.output8)
        self.line3.add_widget(self.output_valide2)
        self.line3.add_widget(self.output_color2)
        self.box.add_widget(self.line4)

        self.line5 = BoxLayout(orientation= 'horizontal')
        self.line5.add_widget(self.output9)
        self.line5.add_widget(self.output10)
        self.line5.add_widget(self.output11)
        self.line5.add_widget(self.output12)
        self.line5.add_widget(self.output_valide3)
        self.line3.add_widget(self.output_color3)
        self.box.add_widget(self.line5)

        self.line6 = BoxLayout(orientation = 'horizontal')
        self.line6.add_widget(self.output13)
        self.line6.add_widget(self.output14)
        self.line6.add_widget(self.output15)
        self.line6.add_widget(self.output16)
        self.line6.add_widget(self.output_valide4)
        self.line3.add_widget(self.output_color4)
        self.box.add_widget(self.line6)

        self.line7 = BoxLayout(orientation = 'horizontal')
        self.line3.add_widget(self.output17)
        self.line3.add_widget(self.output18)
        self.line3.add_widget(self.output19)
        self.line3.add_widget(self.output20)
        self.line3.add_widget(self.output_valide5)
        self.line3.add_widget(self.output_color5)
        self.box.add_widget(self.line7)

        self.line8 = BoxLayout(orientation = 'horizontal')
        self.line3.add_widget(self.output21)
        self.line3.add_widget(self.output22)
        self.line3.add_widget(self.output23)
        self.line3.add_widget(self.output24)
        self.line3.add_widget(self.output_valide6)
        self.line3.add_widget(self.output_color6)
        self.box.add_widget(self.line8)

        self.line9 = BoxLayout(orientation = 'horizontal')
        self.line3.add_widget(self.output25)
        self.line3.add_widget(self.output26)
        self.line3.add_widget(self.output27)
        self.line3.add_widget(self.output28)
        self.line3.add_widget(self.output_valide7)
        self.line3.add_widget(self.output_color7)
        self.box.add_widget(self.line9)
# spinner avec les couleurs 1/6 pour la taille en bas appel la def des couleurs si non marche pas 
        self.line10 = BoxLayout(orientation = 'horizontal')
        self.spinner1 = Spinner(text = 'couleurs',values = ('rouge','vert','bleu','mauve','jaune','turquoise'), size_hint = (1/6,1))
        self.spinner2 = Spinner(text = 'couleurs',values = ('rouge','vert','bleu','mauve','jaune','turquoise'), size_hint = (1/6,1))
        self.spinner3 = Spinner(text = 'couleurs',values = ('rouge','vert','bleu','mauve','jaune','turquoise'), size_hint = (1/6,1))
        self.spinner4 = Spinner(text = 'couleurs',values = ('rouge','vert','bleu','mauve','jaune','turquoise'), size_hint = (1/6,1))
        bouton_valide = Button(text = 'Valide', size_hint= (1/3,1))
        bouton_valide.bind(on_press = lambda c:self.def_colors(self.tours))
        self.line10.add_widget(self.spinner1)
        self.line10.add_widget(self.spinner2)
        self.line10.add_widget(self.spinner3)
        self.line10.add_widget(self.spinner4)
        self.line10.add_widget(bouton_valide)
        self.box.add_widget(self.line10)
        screen.add_widget(self.box)
        return screen

#a refaire en liste et dico cf couleursjuste un random choices 

    def random_couleur(self,aleatoire):
        if aleatoire == 1:
            couleurs = [102/255,0,204/255,1],[0,76/255,153/255,1],[128/255,1,0,1],[1,1,102/255,1],[1,1,102/255,1],[153/255,0,0,1]
            return choices(couleurs, k=4)
        else:
            return self.chosen_colors1

    def select_colors(self,couleurs1,couleurs2,couleurs3,couleurs4,chosen_colors1):   #selection de la couleur
        select = list()
        select.append(couleurs1)
        select.append(couleurs2)
        select.append(couleurs3)
        select.append(couleurs4)
        self.variable = 0
        chosen_colors = deepcopy(chosen_colors1)
        for i in range(len(select)):
            if select[i] in chosen_colors:
                self.variable += 1
                chosen_colors.remove(select[i])
        return self.variable 

    def placement_color(self,couleurs1,couleurs2,couleurs3,couleurs4,chosen_colors): #dis si l emplacement est bon et combien
        select = list()
        select.append(couleurs1)
        select.append(couleurs2)
        select.append(couleurs3)
        select.append(couleurs4)
        self.variable_placement = 0
        for i in range(len(select)):
            if select[i] == chosen_colors[i]:
                self.variable_placement += 1
        return self.variable_placement
        
    def def_colors(self,x): #couleurs avec spinner grosse fonction variable lourde

        if x==1:
            couleurs1 = self._valeur(self.spinner1.text)
            couleurs2 = self._valeur(self.spinner2.text)
            couleurs3 = self._valeur(self.spinner3.text)
            couleurs4 = self._valeur(self.spinner4.text)
            self.output1.Background_color = couleurs1
            self.output2.Background_color = couleurs2
            self.output3.Background_color = couleurs3
            self.output4.Background_color = couleurs4
            self.tours = self.tours+1

            self.chosen_colors1 = self.random_couleur(1)
            self.output_valide1.text = str(self.select_colors(couleurs1,couleurs2,couleurs3,couleurs4,self.chosen_colors1))
            self.output_color1.text = str(self.placement_color(couleurs1,couleurs2,couleurs3,couleurs4,self.chosen_colors1))
            self.output_ratio.text = self.winrate_ratio()

            if self.variable == 4 and self.variable_placement == 4:
                self.ToscreenVictory()
                self.winrate_tot(1)

            

        if x == 2 :
            couleurs1 = self._valeur(self.spinner1.text)
            couleurs2 = self._valeur(self.spinner2.text)
            couleurs3 = self._valeur(self.spinner3.text)
            couleurs4 = self._valeur(self.spinner4.text)
            self.output5.Background_color = couleurs1
            self.output6.Background_color = couleurs2
            self.output7.Background_color = couleurs3
            self.output8.Background_color = couleurs4
            self.tours = self.tours+1

            chosen_colors1 = self.random_couleur(1)
            self.output_valide2.text = str(self.select_colors(couleurs1,couleurs2,couleurs3,couleurs4,self.chosen_colors1))
            self.output_color2.text = str(self.placement_color(couleurs1,couleurs2,couleurs3,couleurs4,self.chosen_colors1))
                
            if self.variable == 4 and self.variable_placement == 4:
                self.ToscreenVictory()
                self.winrate_tot(2)

            
        if x == 3 :
            couleurs1 = self._valeur(self.spinner1.text)
            couleurs2 = self._valeur(self.spinner2.text)
            couleurs3 = self._valeur(self.spinner3.text)
            couleurs4 = self._valeur(self.spinner4.text)
            self.output9.Background_color = couleurs1
            self.output10.Background_color = couleurs2
            self.output11.Background_color = couleurs3
            self.output12.Background_color = couleurs4
            self.tours = self.tours+1

            chosen_colors1 = self.random_couleur(1)
            self.output_valide3.text = str(self.select_colors(couleurs1,couleurs2,couleurs3,couleurs4,self.chosen_colors1))
            self.output_color3.text = str(self.placement_color(couleurs1,couleurs2,couleurs3,couleurs4,self.chosen_colors1))
                
            if self.variable == 4 and self.variable_placement == 4:
                self.ToscreenVictory()
                self.winrate_tot(3)
            

        if x == 4 :
            couleurs1 = self._valeur(self.spinner1.text)
            couleurs2 = self._valeur(self.spinner2.text)
            couleurs3 = self._valeur(self.spinner3.text)
            couleurs4 = self._valeur(self.spinner4.text)
            self.output13.Background_color = couleurs1
            self.output14.Background_color = couleurs2
            self.output15.Background_color = couleurs3
            self.output16.Background_color = couleurs4
            self.tours = self.tours+1

            chosen_colors1 = self.random_couleur(1)
            self.output_valide4.text = str(self.select_colors(couleurs1,couleurs2,couleurs3,couleurs4,self.chosen_colors1))
            self.output_color4.text = str(self.placement_color(couleurs1,couleurs2,couleurs3,couleurs4,self.chosen_colors1))
                
            if self.variable == 4 and self.variable_placement == 4:
                self.ToscreenVictory()
                self.winrate_tot(4)


        if x == 5 :
            couleurs1 = self._valeur(self.spinner1.text)
            couleurs2 = self._valeur(self.spinner2.text)
            couleurs3 = self._valeur(self.spinner3.text)
            couleurs4 = self._valeur(self.spinner4.text)
            self.output17.Background_color = couleurs1
            self.output18.Background_color = couleurs2
            self.output19.Background_color = couleurs3
            self.output20.Background_color = couleurs4
            self.tours = self.tours+1

            chosen_colors1 = self.random_couleur(1)
            self.output_valide5.text = str(self.select_colors(couleurs1,couleurs2,couleurs3,couleurs4,self.chosen_colors1))
            self.output_color5.text = str(self.placement_color(couleurs1,couleurs2,couleurs3,couleurs4,self.chosen_colors1))
                
            if self.variable == 4 and self.variable_placement == 4:
                self.ToscreenVictory()
                self.winrate_tot(5)

        if x == 6 :
            couleurs1 = self._valeur(self.spinner1.text)
            couleurs2 = self._valeur(self.spinner2.text)
            couleurs3 = self._valeur(self.spinner3.text)
            couleurs4 = self._valeur(self.spinner4.text)
            self.output21.Background_color = couleurs1
            self.output22.Background_color = couleurs2
            self.output23.Background_color = couleurs3
            self.output24.Background_color = couleurs4
            self.tours = self.tours+1

            chosen_colors1 = self.random_couleur(1)
            self.output_valide6.text = str(self.select_colors(couleurs1,couleurs2,couleurs3,couleurs4,self.chosen_colors1))
            self.output_color6.text = str(self.placement_color(couleurs1,couleurs2,couleurs3,couleurs4,self.chosen_colors1))
                
            if self.variable == 4 and self.variable_placement == 4:
                self.ToscreenVictory()
                self.winrate_tot(6)

        if x == 7 :
            couleurs1 = self._valeur(self.spinner1.text)
            couleurs2 = self._valeur(self.spinner2.text)
            couleurs3 = self._valeur(self.spinner3.text)
            couleurs4 = self._valeur(self.spinner4.text)
            self.output25.Background_color = couleurs1
            self.output26.Background_color = couleurs2
            self.output27.Background_color = couleurs3
            self.output28.Background_color = couleurs4
            self.tours = self.tours+1

            chosen_colors1 = self.random_couleur(1)
            self.output_valide7.text = str(self.select_colors(couleurs1,couleurs2,couleurs3,couleurs4,self.chosen_colors1))
            self.output_color7.text = str(self.placement_color(couleurs1,couleurs2,couleurs3,couleurs4,self.chosen_colors1))
                
            if self.variable != 4 and self.variable_placement != 4 : #perd fenetre defaite
                self.ToscreenDefeat()
            if self.variable == 4 and self.variable_placement == 4: #gagne
                self.ToscreenVictory()  #ouvre la fenetre win
                self.winrate_tot(7)      #montre le total

    def winrate_tot(self,nombre_de_chance): #voir fichier json cours
        try:
            with open('ratio.json') as file:
                ratio = json.loads(file.read())
        except FileNotFoundError:
            ratio = list()
        ratio.append('{}({})'.format(nombre_de_chance,str(self.input1.text)))


        with open("ratio.json", 'w') as file:
            file.write(json.dumps(contacts, indent='\t'))

    def winrate_ratio(self): #voir fichier json cours
        try:
            with open('ratio.json') as file:
                list_ratio = json.loads(file.read())
                ratio = self.ratio1(list_ratio)
                return ratio
        except FileNotFoundError:
            return "Aucune Partie Sauvegarde"
    def ratio1(self,liste):        #ajout du ratio
        res = list()
        for i in range(len(liste)):
            res.append(liste[i].split(''))

        for i in range(len(res)-1):
            if res[0][0]<res[1][0]:
                res.remove(res[1])
            else :
                res.remove(res[0])
        return ''.join(res[0])

    def _valeur(self,res): # 6 couleurs dispo on reconnait que la premiere lettre 
        indice = list(res)
        if indice[0] == 'r':
            return [153/255,0,0,1]
        if indice[0] == 'b':
            return [0,76/255,153/255,1]
        if indice[0] == 'v':
            return [128/255,1,0,1]
        if indice[0] == 'm':
            return [102/255,0,204/255,1]
        if indice[0] == 't':
            return [0,204/255,204/255,1]
        if indice[0] == 'j':
            return [1,1,102/255,1]

#differents screen avec images  attention a l ordre popur le widget

    def ScreenMenu(self):
        screen = Screen(name = 'Menu')
        box = BoxLayout(orientation ='vertical')
        box.add_widget(Label(text='Bienvenu dans le Jeu MasterMind',
        font_size = 32,
        size_hint_y=0.1,
        height=70,
        size_hint_x = 1,
        width = 250))
        box.add_widget(AsyncImage(source = 'images/master.png'))
        bouton = Button(text='Play the game',
        font_size = 32,
        size_hint_y=0.1,
        height=70,
        size_hint_x = 1,
        width = 250)
        bouton.background_color = [102/255,0,204/255,1]
        bouton.add_widget(AsyncImage(source = 'images/bouttonmenu'))
        bouton.bind(on_press = self.ToscreenGame)
        box.add_widget(bouton)
        screen.add_widget(box)
        return screen

    def ScreenVictory(self):
        screen = Screen(name = 'Victory')
        box = BoxLayout(orientation ='vertical')
        box.add_widget(AsyncImage(source = 'images/victory.png'))
        line1 = BoxLayout(orientation = 'horizontal')
        bouton = Button(text='Back to Menu',
        font_size = 32,
        size_hint_y=0.5,
        height=70,
        size_hint_x = 1,
        width = 250)
        bouton.background_color = [0,76/255,153/255,1]
        bouton.bind(on_press = self.ToscreenMenu)
        line1.add_widget(bouton)
        bouton_stop = Button(text = ' Stop the Game',
        font_size = 32,
        size_hint_y=0.5,
        height=70,
        size_hint_x = 1,
        width = 250)
        bouton_stop.background_color = [102/255,0,204/255,1]
        bouton_stop.bind(on_press = self.fermergame)
        bouton_stop.add_widget(AsyncImage(source = 'images/bouttonmenu'))
        line1.add_widget(bouton_stop)
        box.add_widget(line1)
        screen.add_widget(box)
        return screen

    def ScreenDefeat(self):
        screen = Screen(name = 'Defeat')
        box = BoxLayout(orientation ='vertical')
        box.add_widget(AsyncImage(source = 'images/defeat.png')) #Async pour image dans le fichier
        line1 = BoxLayout(orientation = 'horizontal')
        bouton = Button(text='Back to Menu',                 #emplacement sur la map tous les memes
        font_size = 32,
        size_hint_y=0.5,
        height=70,
        size_hint_x = 1,
        width = 250)
        bouton.background_color = [0,76/255,153/255,1]      #bleu
        bouton.bind(on_press = self.ToscreenMenu)
        line1.add_widget(bouton)
        bouton_stop = Button(text = ' Stop the Game',
        font_size = 32,
        size_hint_y=0.5,
        height=70,
        size_hint_x = 1,
        width = 250)
        bouton_stop.background_color = [102/255,0,204/255,1] #mauve
        bouton_stop.bind(on_press = self.fermergame)
        bouton_stop.add_widget(AsyncImage(source = 'images/bouttonmenu'))
        line1.add_widget(bouton_stop)
        box.add_widget(line1)
        screen.add_widget(box)
        return screen

    def ToscreenMenu(self,source):
        self.manager.current = "Menu"
    
    def ToscreenGame(self,source):
        self.manager.current = "Game"

    def ToscreenVictory(self):
        self.manager.current = "Victory"
    
    def ToscreenDefeat(self): #defaite ou Defeat ?
        self.manager.current = "Defeat"

    def fermergame(self,source): #sort de la partie
        exit()

#on remet les boutons a zero pour recommencer 28 output 7 valide couleurs attention aux tours

    def remetre_variable_a_zero(self):
        self.tours = 1

        self.output_ratio.text = self.winrate_ratio()
        self.output1.background_color = [0,0,0,0]
        self.output2.background_color = [0,0,0,0]
        self.output3.background_color = [0,0,0,0]
        self.output4.background_color = [0,0,0,0]
        self.output_valide1.text = ''
        self.output_color1.text = ''

        self.output_ratio.text = self.winrate_ratio()
        self.output5.background_color = [0,0,0,0]
        self.output6.background_color = [0,0,0,0]
        self.output7.background_color = [0,0,0,0]
        self.output8.background_color = [0,0,0,0]
        self.output_valide2.text = ''
        self.output_color2.text = ''

        self.output_ratio.text = self.winrate_ratio()
        self.output9.background_color = [0,0,0,0]
        self.output10.background_color = [0,0,0,0]
        self.output11.background_color = [0,0,0,0]
        self.output12.background_color = [0,0,0,0]
        self.output_valide3.text = ''
        self.output_color3.text = ''

        self.output_ratio.text = self.winrate_ratio()
        self.output13.background_color = [0,0,0,0]
        self.output14.background_color = [0,0,0,0]
        self.output15.background_color = [0,0,0,0]
        self.output16.background_color = [0,0,0,0]
        self.output_valide4.text = ''
        self.output_color4.text = ''

        self.output_ratio.text = self.winrate_ratio()
        self.output17.background_color = [0,0,0,0]
        self.output18.background_color = [0,0,0,0]
        self.output19.background_color = [0,0,0,0]
        self.output20.background_color = [0,0,0,0]
        self.output_valide5.text = ''
        self.output_color5.text = ''

        self.output_ratio.text = self.winrate_ratio()
        self.output21.background_color = [0,0,0,0]
        self.output22.background_color = [0,0,0,0]
        self.output23.background_color = [0,0,0,0]
        self.output24.background_color = [0,0,0,0]
        self.output_valide6.text = ''
        self.output_color6.text = ''

        self.output_ratio.text = self.winrate_ratio()
        self.output25.background_color = [0,0,0,0]
        self.output26.background_color = [0,0,0,0]
        self.output27.background_color = [0,0,0,0]
        self.output28.background_color = [0,0,0,0]
        self.output_valide7.text = ''
        self.output_color7.text = ''

#lancement du jeu

MastermindApp().run()

    

    

    

    



        

            



        


