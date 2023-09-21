from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button

from creating_training_screen import CreatingTrainingScreen

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = "vertical"
        
        self.create_training_button = CreateTrainingButton(on_release = self.open_create_training_screen)
        self.choose_training_button = ChooseTrainingButton()
        
        self.add_widget(self.create_training_button)
        self.add_widget(self.choose_training_button)
        
    def open_create_training_screen(self, instance):
        screen_manager = App.get_running_app().root
        screen_manager.transition.direction = 'left'
        screen_manager.current = "Создание тренировки"

class CreateTrainingButton(Button):
    def __init__(self, **kwargs):
        super(CreateTrainingButton, self).__init__(**kwargs)
        self.text = "Создать тренировку"
        self.font_size = 12
        self.background_color = [1, 0.976, 0, 1]
        self.size_hint = (None, None)
        self.size = (150, 50)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.9}

class ChooseTrainingButton(Button):
    def __init__(self, **kwargs):
        super(ChooseTrainingButton, self).__init__(**kwargs)
        self.text = "Выбрать тренировку"
        self.font_size = 12
        self.background_color = [1, 0.976, 0, 1]
        self.size_hint = (None, None)
        self.size = (150, 50)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.8}

if __name__ == "__main__":
    scr = MainScreen()
    print(dir(scr))