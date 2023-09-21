from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button

from go_back_button import GoBackButton

class ChooseTrainingScreen(Screen):
    def __init__(self, **kwargs):
        super(ChooseTrainingScreen, self).__init__(**kwargs)
        self.orientation = "vertical"
        
        self.back_button = GoBackButton(on_release = self.go_back)
        
        self.add_widget(self.back_button)
        
    def go_back(self, instance):
        screen_manager = App.get_running_app().root
        screen_manager.transition.direction = 'right'
        screen_manager.current = "Главный экран"
