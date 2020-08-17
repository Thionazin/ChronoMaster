#Thar be imports
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout 


#Creation of the main app class
class chrono_master(App):
    def build(self):
        #Layout of the whole thing
        mainlayout = BoxLayout(orientation = 'vertical')
        butlayout = BoxLayout(orientation = 'horizontal')

        backbutton = Button(text = '<-')
        forbutton = Button(text = '->')

        butlayout.add_widget(backbutton)
        butlayout.add_widget(forbutton)

        #Layout of calendar portion
        layout = GridLayout(cols=7, rows=5)
        #Making each button on the layout
        for i in range(1, 36):
            layout.add_widget(Button(text = str(i)))

        mainlayout.add_widget(butlayout)
        mainlayout.add_widget(layout)

        return mainlayout


chrono_master().run()