class LinearInterpolation:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def calc(self, x: float) -> int:
        if x <= self.x1:
            return self.y1
        elif x >= self.x2:
            return self.y2
        return round(
            self.y1 + ((self.y2 - self.y1) / (self.x2 - self.x1)) * (x - self.x1)
        )
