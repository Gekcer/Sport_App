from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle

from create_training_button import CreateTrainingButton
from choose_training_button import ChooseTrainingButton

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = "vertical"
        
        create_training_button = CreateTrainingButton()
        choose_training_button = ChooseTrainingButton()
        
        self.add_widget(create_training_button)
        self.add_widget(choose_training_button)
        
        # print(dir(self.canvas))
        
if __name__ == "__main__":
    scr = MainScreen()
    print(dir(scr))