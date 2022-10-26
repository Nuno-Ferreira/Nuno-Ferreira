"""
My first application that converts any currency in seconds
"""
from lib2to3.pytree import convert
import toga
from toga.style.pack import COLUMN, ROW, LEFT, RIGHT, Pack
from currency_converter import currency_converter
#import android
#from android.util import Log
#from android.widget import LinearLayout
#from android.widget import Button
#from android.widget import TextView
#from android.view import Gravity
#import android.view



#lets start again but with toga

def build(app):
    c1_box = toga.Box()
    c2_box = toga.Box()
    box = toga.Box()

    c1_input = toga.TextInput(readonly=True)
    c2_input = toga.TextInput()

    c1_label = toga.Label('GBP', style=Pack(text_align=RIGHT))
    c2_label = toga.Label('EUR', style=Pack(text_align=RIGHT))
    join_label = toga.Label('converts to', style=Pack(text_align=RIGHT))

   # def convert(widget): #make this connnect to the currencyconverter script



    button = toga.Button('Convert', on_press=convert)

    c2_box.add(c2_input)
    c2_box.add(c2_label)

    c1_box.add(join_label)
    c1_box.add(c1_input)
    c1_box.add(c1_label)

    box.add(c2_box)
    box.add(c1_box)
    box.add(button)

    #this where the styling happens, it looks similar to CSS
    box.style.update(direction=COLUMN, padding_top=10)
    c2_box.style.update(direction=ROW, padding=5)
    c1_box.style.update(direction=ROW, padding=5)

    c1_input.style.update(flex=1)
    c2_input.style.update(flex=1, padding_left=160)
    c1_label.style.update(width=100, padding_left=10)
    c2_label.style.update(width=100, padding_left=10)
    join_label.style.update(width=150, padding_right=10)

    button.style.update(padding=15, flex=1)

    return box



#this was a mistake // this is if I was trying ot build with VOC (another transpiler)
"""
class ButtonClick(implements=android.view.View[OnClickListener]):
    def __init__(self, callback, *args, **kwargs):
        self.callback = callback
        self.args = args
        self.kwargs = kwargs

    def onClick(self, view: android.view.View) -> void:
        self.callback(*self.args, **self.kwargs)


class CurrencyConverter:
    def __init__(self):
        self.activity = android.PythonActivity.setListener(self)
        self.buttons = []
        

    def onCreate(self):
        
        self.convert_button = Button(self._activity)
        self.convert_button.setText('Convert')
        self.convert_button.setOnClickListener(ButtonClick(self.convert_currency)) #this will make the connection for the app to convert
        vlayout.addView(self.convert_button)

        footer = TextView(self._activity) #this will set the footer and the self_activity will communicate with pythonactivity 
        footer = setText('Powered by Python')
        footer.setGravity(Gravity.CENTER) #this will position the text
        vlayout.addView(footer) #still need to find out what it does but maybe it adds it to the screen

    def convert_currency(self):
        self.activity
        self.message = None
        self.runScript()

    def runScript(self):


#might need this in the future to build the toga app

class CurrencyConverter(toga.App):
    def __init__(self):
        self.buttons = []
        

    def startup(self):
        
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        
        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            'Your name: ',
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            'Say Hello!',
            on_press=self.say_hello,
            style=Pack(padding=5)
        )

        main_box.add(name_box)
        main_box.add(button)



        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


    def say_hello(self, widget):
        print("Hello,", self.name_input.value)
"""


def main():
    return CurrencyConverter()






