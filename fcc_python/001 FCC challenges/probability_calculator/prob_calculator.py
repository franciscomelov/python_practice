import copy
import random


class Hat:
    def __init__(self, **kargs) -> None:
        self.balls = [name for name, number in kargs.items() for number in range(number)]
        self.contents = copy.copy(self.balls)


    def draw(self, n_balls):
        if n_balls > len(self.balls):
            return self.contents

        self.contents = copy.copy(self.balls)
        pulled_balls=[]

        for _ in range(n_balls):
            idx = random.randint(0,len(self.contents)-1)
            pulled_balls.append(self.contents.pop(idx))

        return pulled_balls

def list_to_dict(dictionary):
    result ={}
    for ball in dictionary:
        result[ball] = result.get(ball, 0) +1
    return result

def test_match(expected_balls,pulled_balls):
    matches =0
    dict_pulled =list_to_dict(pulled_balls)

    loop=True
    while loop:
        
        for color  in expected_balls:
            if dict_pulled.get(color, False):#check if ball is in hat
                if expected_balls[color]>dict_pulled[color]:#Check number of balls in hat and take if posible
                    loop =False
                dict_pulled[color] -= expected_balls[color]
            else:
                loop =False

        if not loop: break
        matches+=1
    return matches



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    match_balls=0
    for _ in range(num_experiments):
        pulled_balls = hat.draw(num_balls_drawn)

        match_balls +=test_match(expected_balls, pulled_balls)

    return match_balls/num_experiments



