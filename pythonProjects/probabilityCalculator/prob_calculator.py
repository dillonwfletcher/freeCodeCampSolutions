import copy
import random

class Hat:

    def __init__(self, **kwargs):
        balls = kwargs
        self.contents = []
        for k, v in balls.items():
            while v > 0:
                self.contents.append(k)
                v-=1
    
    def draw(self, num):
        if num >= len(self.contents):
            return self.contents

        drawn, track = [], []
        
        while num > 0:
            idx = random.randint(0, len(self.contents)-1)
            drawn.append(self.contents[idx])
            del self.contents[idx]
            num -= 1

        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    m, n = 0, 0
    while n < num_experiments:
        
        hat_copy = copy.deepcopy(hat)

        drawn = hat_copy.draw(num_balls_drawn)
        drawn_balls = {}
        for color in drawn:
            if drawn_balls.get(color) == None:
                drawn_balls[color] = 1
                continue
            drawn_balls[color] += 1
        
        match = True
        for k, v in expected_balls.items():

            if drawn_balls.get(k) == None or drawn_balls[k] < v:
                match = False
                break

        if match: m += 1

        n += 1

        
    return m/num_experiments
