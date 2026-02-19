class Car:
    """Задача: car"""
    def __init__(self):
        self.speed = 0

    def accelerate(self, v: int):
        pass

    def brake(self, v: int):
        """Снижает скорость, но не ниже 0"""
        if v > 0:
            v =- 1
        pass
