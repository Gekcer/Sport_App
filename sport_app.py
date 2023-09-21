from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen

from main_screen import MainScreen
from trainings_manager import TrainingsManager
from creating_training_screen import CreatingTrainingScreen
from choose_training_screen import ChooseTrainingScreen

class SportApp(App):
    def build(self):
        self.trainings_manager = TrainingsManager()
        
        self.prepare_screens()
        return self.screen_manager
    
    def prepare_screens(self):
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(MainScreen(name = "Главный экран"))
        self.screen_manager.add_widget(CreatingTrainingScreen(name = "Создание тренировки"))
        self.screen_manager.add_widget(ChooseTrainingScreen(name = "Выбор тренировки"))

if __name__ == '__main__':
    Config.set('graphics', 'width', '240')
    Config.set('graphics', 'height', '520')
    SportApp().run()