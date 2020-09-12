import agent
import numpy
import random

class Oekosystem:

    def __init__(self):
        self.agents = []
        for i in range(100):
            self.agents.append(Agent())

    def deathmatch(self, max, min):
        score = (0,0)
        

    def main(self):
        round = 0
        while(round != 1000):
            random.shuffle(agents)
            for i in range(50):
                max = agents.pop(0)
                min = agents.pop(0)
                self.deathmatch(max, min)

    def winner(self, v):
        for i in range(3):
            if v[i] == v[i+3] and v[i] == v[i+6]:
                return v[i]
            i *= 3
            if v[i] == v[i+1] and v[i] == v[i+2]:
                return v[i]
        if v[0] == v[4] and v[4] == v[8]:
            return v[0]
        if v[2] == v[4] and v[4] == v[6]:
            return v[0]
        return 0