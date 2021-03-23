import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        self.copy = []

        for color, n in kwargs.items():
            #self.contents+=[color] * n
            self.copy+=[color] * n
            self.contents = self.copy.copy()

    def draw(self, n):
        self.contents = self.copy.copy()
        if n > len(self.contents): return self.contents
        drawn = random.sample(self.contents,k=n)
        for color in drawn:
            self.contents.remove(color)
        
        return drawn

def experiment(**kwargs):

    (hat, expected_balls, num_balls_drawn, num_experiments) = kwargs.values()

    M = 0
    i = num_experiments
    while i > 0:
        drawnBalls = hat.draw(num_balls_drawn)
        drawnBallsDict = dict()
        
        for color, n in expected_balls.items():
            if color in drawnBalls and drawnBalls.count(color) >= n:
                drawnBallsDict[color] =  n
        if drawnBallsDict == expected_balls: M+=1
        i-=1
    return M/num_experiments