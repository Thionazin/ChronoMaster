#Thar be imports
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import datetime


#Creation of the main app class
class borsurth(App):
    def build(self):
        #Layout of the whole thing
        main_layout = BoxLayout(orientation = 'vertical')
        but_layout = BoxLayout(orientation = 'horizontal')
        upper_layout = BoxLayout(orientation = 'vertical')

        self.countdown_timer = Label(text = 'sample')

        Clock.schedule_interval(self.countdown, 1)


        back_button = Button(text = '<-')
        year_label = Label(text = 'Sample Text')
        for_button = Button(text = '->')

        but_layout.add_widget(back_button)
        but_layout.add_widget(year_label)
        but_layout.add_widget(for_button)

        #Layout of calendar portion
        layout = GridLayout(cols=7, rows=5)
        #Making each button on the layout
        for i in range(1, 36):
            layout.add_widget(Button(text = str(i)))

        upper_layout.add_widget(self.countdown_timer)
        upper_layout.add_widget(but_layout)
        main_layout.add_widget(upper_layout)
        main_layout.add_widget(layout)

        return main_layout

    def countdown(self, dt):
        self.countdown_timer.text = str(datetime.datetime.now())


if __name__ == '__main__': 
    borsurth().run()