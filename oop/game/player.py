class Player:
    def __init__(self, name):
        self.name = name
        self._level = 1
        self._lives = 3
        self._score = 0

    # ------------------ Lives property ------------------
    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, value):
        if value >= 0:
            self._lives = value
        else:
            print("Lives cannot be negative")
            self._lives = 0

    # ------------------ Level property ------------------
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if value > 0:
            delta = value - self._level
            self._score += delta * 1000  # update score
            self._level = value
        else:
            print("Level can't be less than 1")

    # ------------------ Score property ------------------
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if value >= 0:
            self._score = value
        else:
            print("Score cannot be negative")
            self._score = 0

    # ------------------ String representation ------------------
    def __str__(self):
        return f"Name: {self.name}, Lives: {self.lives}, Level: {self.level}, Score: {self.score}"
