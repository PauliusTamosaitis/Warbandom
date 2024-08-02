class Player:
    def __init__(self, name):
        self.name = name
        self.total_score = 0

    def add_point(self):
        self.total_score += 1