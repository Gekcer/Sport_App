from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
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
        self.add_exercisse_button = AddExerciseButton(on_release = self.add_exercise)
        
        self.add_widget(self.back_button)
        self.add_widget(self.add_exercisse_button)
        
    '''
    События кнопок
    '''
    def go_back(self, instance):
        screen_manager = App.get_running_app().root
        screen_manager.transition.direction = 'right'
        screen_manager.current = "Главный экран"
    
    def add_exercise(self, instance):
        print('len =', len(self.entrys))
        print(self.entrys[0].text)
        print(type(self.entrys[0].text))
        print(len(self.entrys[0].text))
        print('here')
        print('here')
        print('here')
        print('here')
        for entry in self.entrys:
            if not entry.text.strip() == "":        
                trainings_manager = App.get_running_app().trainings_manager
                name = self.entrys[0].text
                exercise = [self.entrys[1], self.entrys[2], self.entrys[3]]
                trainings_manager.add_training(name, exercise)
                
                popup = TrainingPopup('Тренировка/упражнение добавлено')
                popup.open()
            else:
                popup = TrainingPopup('Пустое поле')
                popup.open()
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

class AddExerciseButton(Button):
    def __init__(self, **kwargs):
        super(AddExerciseButton, self).__init__(**kwargs)
        self.text = "+"
        self.font_size = 12
        self.background_color = [1, 1, 1, 1]
        self.size_hint = (None, None)
        self.size = (60, 25)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.46}
        
class TrainingPopup(Popup):
    def __init__(self, message, **kwargs):
        super(TrainingPopup, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical')
        label = Label(text=message)
        button = Button(text='Ок', size_hint=(1, 0.2))
        button.bind(on_release=self.dismiss)
        
        layout.add_widget(label)
        layout.add_widget(button)
        
        self.content = layout