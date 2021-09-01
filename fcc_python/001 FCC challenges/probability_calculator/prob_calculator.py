import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kargs) -> None:
        self.balls = kargs
        self.contents = [name for name, number in kargs.items() for number in range(number)]
    
    def show_balls(self):
        print(self.contents)
    
    def draw(self, n_balls):
        urn = copy.copy(self.contents)
        print("urn: ", urn)
        pulled_balls=[]
        while len(urn)>=n_balls:
            pulling=[]
            for _ in range(n_balls):
                idx = random.randin,,-´pññññññ´ñ[Ppp{:}].t(0,len(urn)-1)
                pulling.append(urn.pop(idx))
            pulled_balls.append(pulling)
            print("urn: ", urn)
            print("pulled:",pulled_balls)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    match_balls=0
    for _ in range(num_experiments):
        hat.draw(num_balls_drawn)
    pass

hat = Hat(black=6, red=4, green=3)

hat.draw(3)

# probability = experiment(hat=hat, 
#                   expected_balls={"red":2,"green":1},
#                   num_balls_drawn=5,
#                   num_experiments=2000)
