from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget

Window.size = (600, 800)
Window.clearcolor = (1, 1, 1, 1)

class FormatterApp(App):
    def build(self):
        return FormatterLayout()

class FormatterLayout(BoxLayout):
    def spinner_clicked(self, text):
        print(text)

    def change_color(self, red_slider, green_slider, blue_slider):
        Window.clearcolor = (red_slider, green_slider, blue_slider, 1)

    def color_switch(self, value):
        if value:
            self.color_switcher_label.color = (1, 1, 1, 1)
            self.spinner.color = (1, 1, 1, 1)
            self.main_label.color = (1, 1, 1, 1)
            self.khakis.color = (1, 1, 1, 1)
            self.jeans.color = (1, 1, 1, 1)
            self.sweatpants.color = (1, 1, 1, 1)
            self.pick1.color = (1, 1, 1, 1)
            self.red_label.color = (1, 1, 1, 1)
            self.blue_label.color = (1, 1, 1, 1)
            self.green_label.color = (1, 1, 1, 1)
        else:
            self.color_switcher_label.color = (0, 0, 0, 1)
            self.spinner.color = (0, 0, 0, 1)
            self.main_label.color = (0, 0, 0, 1)
            self.khakis.color = (0, 0, 0, 1)
            self.jeans.color = (0, 0, 0, 1)
            self.sweatpants.color = (0, 0, 0, 1)
            self.pick1.color = (0, 0, 0, 1)
            self.red_label.color = (0, 0, 0, 1)
            self.blue_label.color = (0, 0, 0, 1)
            self.green_label.color = (0, 0, 0, 1)

if __name__ == "__main__":
    formatter = FormatterApp()
    formatter.run()