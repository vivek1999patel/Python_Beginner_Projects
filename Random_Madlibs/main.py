import hp, hungergames, code, zombie;
import random

def random_madlibs():
    m = random.choice([hp, code, zombie, hungergames])
    return m.madlib()

random_madlibs()