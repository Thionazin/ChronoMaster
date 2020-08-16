#Thar be imports
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button 


#Creation of the main app class
class chrono_master(App):
    def build(self):
        #Layout of calendar portion
        layout = GridLayout(cols=7, rows=5)
        #Making each button on the layout
        for i in range(1, 36):
            layout.add_widget(Button(text = str(i)))
        return layout


chrono_master().run()