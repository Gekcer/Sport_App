from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button

class CreatingTrainingScreen(Screen):
    def __init__(self, **kwargs):
        super(CreatingTrainingScreen, self).__init__(**kwargs)
        self.orientation = "vertical"
        
        self.back_button = GoBackButton(on_release = self.go_back)
        
        self.add_widget(self.back_button)
        
    def go_back(self, instance):
        screen_manager = App.get_running_app().root
        screen_manager.transition.direction = 'right'
        screen_manager.current = "Главный экран"
    
class GoBackButton(Button):
    def __init__(self, **kwargs):
        super(GoBackButton, self).__init__(**kwargs)
        self.text = "Назад"
        self.font_size = 12
        self.background_color = [1, 0.976, 0, 1]
        self.size_hint = (None, None)
        self.size = (150, 50)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.9}