class TrainingsManager:
    def __init__(self):
        self.trainings = {}
        
    def add_training(self, name, exercise):
        self.trainings[name] = exercise
        return self
        
if __name__ == "__main__":
    training = TrainingsManager()