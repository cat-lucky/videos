import random

def randomColor():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))
