class Player:
    """Задача: player"""
    def __init__(self, name: str):
        self.name = name
        self.score = 0

    def add_score(self, points: int):
        while  self.score < 10:
            self.score += 1
        pass
