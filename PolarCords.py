import math
class Point:
    def __init__(self, a = 0, b = 0): # constructor
        self.r = math.sqrt(a**2 + b**2)
        if a == 0: self.theta = math.pi/2
        else: self.theta = math.atan(b/a) # gives (r, theta) form of point

    def odistance(self):
        return self.r # ez
    
    def translate(self, dx, dy):
        x = self.r*math.cos(self.theta)
        y = self.r*math.sin(self.theta)

        x += dx
        y += dy

        self.r = math.sqrt(x**2+y**2)
        if x == 0: self.theta = math.pi/2
        else: self.theta = math.atan(y/x) # gives (r, theta) form of point