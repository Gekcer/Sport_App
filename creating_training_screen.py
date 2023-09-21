from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput

from go_back_button import GoBackButton

class CreatingTrainingScreen(Screen):
    def __init__(self, **kwargs):
        super(CreatingTrainingScreen, self).__init__(**kwargs)
        self.orientation = "vertical"
        
        self.entrys = []
        self.create_start_forms()
        self.back_button = GoBackButton(on_release = self.go_back)
        self.add_exercisse_button = Button
        
        self.add_widget(self.back_button)
        
    '''
    События кнопок
    '''
    def go_back(self, instance):
        screen_manager = App.get_running_app().root
        screen_manager.transition.direction = 'right'
        screen_manager.current = "Главный экран"
    
    def add_exercise(self, instance):
        print(self.entrys)
    
    '''
    Прочее
    '''
    def create_start_forms(self):
        hint_texts = ['Название тренировки', 'Название упражнения',
                      'Количество подходов', 'Количество повторений']
        pos_hints = [{"center_x": 0.5, "center_y": 0.86}, {"center_x": 0.5, "center_y": 0.76},
                     {"center_x": 0.5, "center_y": 0.66}, {"center_x": 0.5, "center_y": 0.56}]
        sizes = [(150, 50), (150, 50), (150, 50), (150, 50)]
        
        for text, pos, size in zip(hint_texts, pos_hints, sizes):
            entry = TrainEntry(hint_text = text, pos_hint = pos, size = size)
            self.entrys.append(entry)
            self.add_widget(entry)
        return self
        
class TrainEntry(TextInput):
    def __init__(self, **kwargs):
        super(TrainEntry, self).__init__(**kwargs)
        self.font_size = 12
        self.size_hint = (None, None)
