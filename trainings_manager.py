class TrainingsManager:
    def __init__(self):
        self.trainings = {}
        
    def add_training(self, name, exercise):
        if not name in self.trainings.keys():
            self.trainings[name] = []
            self.trainings[name].append(exercise)
        else:
            self.trainings[name].append(exercise)
        return self

if __name__ == "__main__":
    tr = TrainingsManager