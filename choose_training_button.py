from kivy.uix.button import Button

class ChooseTrainingButton(Button):
    def __init__(self, **kwargs):
        super(ChooseTrainingButton, self).__init__(**kwargs)
        self.text = "Выбрать тренировку"
        self.font_size = 12
        self.background_color = [1, 0.976, 0, 1]
        self.size_hint = (None, None)
        self.size = (150, 50)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.8}