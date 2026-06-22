class Point: # template
    def __init__(self, a = 0, b = 0): # parameters
        self.x = a
        self.y = b

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def odistance(self):
        import math
        d = math.sqrt(self.x ** 2 + self.y ** 2)
        return d
    
    def __str__(self):
        return(
            '(' + str(self.x) + ',' + str(self.y) + ')'
        )