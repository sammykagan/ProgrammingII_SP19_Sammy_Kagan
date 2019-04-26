# Kivy Four Function calculator (35pts)
# emulate the built in MACOS calculator app as best you can.

# GENERAL LAYOUT (10pts)
# Make a GridLayout with 6 rows
# Place a text input for the display in the first row
# Row 2 through 6 will be BoxLayouts which will contain buttons.
# Make a custom button class to simplify your kv file.

# FUNCTIONALITY (15pts)
# When you press each button, the text is added to the display (see class example)
# When you press the equal button, the displayed equation will be calculated and will now show the answer using the eval() function
# When the equation cannot be evaluated, it will show "ERROR"
# All buttons will be functional.


# FORMATTING (10pts
# Make it look and feel like the MACOS calculator as closely as possible.
# IMPORTANT: You can change the  +/- and % buttons to something else if you want. (maybe exponent?, maybe open close parentheses?)
# Include spacing and padding as necessary within the grid.
# Match the button colors as closely as you can (orange, gray, white etc)
# Match the font and text color as closely as you can.
# Match the size of the app and the relative button sizes as closely as you can.
# Match the button layout as closely as you can.

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (300, 400)
equal_press = False

class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()

class CalculatorLayout(BoxLayout):
    # all my fuctions go in here (root widget)
    # add a "Try Except"
    def calculate(self, equation):
        try:
            answer = round(eval(equation), 5)
            self.display.text = str(answer)
        except:
            self.display.text = ""
            equal_press = True

    def equal_sign(self):
        equal_press = True

    def equal_check(self):
        if equal_press is True:
            self.display.text = ""



if __name__ == "__main__":
    app = CalculatorApp()
    app.run()