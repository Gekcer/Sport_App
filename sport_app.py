from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from main_screen import MainScreen
from creating_training_screen import CreatingTrainingScreen

class SportApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name = "Главный экран"))
        screen_manager.add_widget(CreatingTrainingScreen(name = "Создание тренировки"))
        return screen_manager

if __name__ == '__main__':
    SportApp().run()