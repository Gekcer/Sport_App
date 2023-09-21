from kivy.uix.button import Button

class GoBackButton(Button):
    def __init__(self, **kwargs):
        super(GoBackButton, self).__init__(**kwargs)
        self.text = "Назад"
        self.font_size = 12
        self.background_color = [1, 1, 1, 1]
        self.size_hint = (None, None)
        self.size = (60, 25)
        self.pos_hint = {"center_x": 0.1, "center_y": 0.98}