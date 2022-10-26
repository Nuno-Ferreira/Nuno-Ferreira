"""
My first application that converts any currency in seconds
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import android
from android.util import Log
from android.widget import LinearLayout
from android.widget import Button
from android.widget import TextView
from android.view import Gravity
import android.view
from currency_converter import currency_converter


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
        

"""
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






