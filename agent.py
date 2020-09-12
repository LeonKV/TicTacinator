import numpy
import random


class Agent:

    def __init__(self, agent=None):
        if agent is None:
            self.age = 0
            self.score = 0
            ran = random.Random()
            self.weights1 = numpy.eye(9)
            for i in range(9):
                for j in range(9):
                    self.weights1[i][j] = ran.uniform(-1, 1)

            self.weights2 = numpy.eye(9)
            for i in range(9):
                for j in range(9):
                    self.weights2[i][j] = ran.uniform(-1, 1)
        else:
            self.score = 0
            self.age = 0
            self.weights1 = agent.weights1.copy()
            self.weights2 = agent.weights2.copy()

    def move_max(self, input):
        options = numpy.matmul(self.weights2, (numpy.matmul(self.weights1, input)))
        index = 0
        max = -1000

        for i in range(9):
            if input[i] == 0:
                if options[i] > max:
                    max = options[i]

        for i in options:
            if i == max:
                return index
            index += 1

    def move_min(self, input):
        options = numpy.matmul(self.weights2, (numpy.matmul(self.weights1, input)))
        index = 0
        min = 1000

        for i in range(9):
            if input[i] == 0:
                if options[i] < min:
                    min = options[i]

        for i in options:
            if i == min:
                return index
            index += 1

    def normalisation(self):
        for i in range(9):
            sum = 0
            for j in range(9):
                sum += abs(self.weights1[i][j])
            for j in range(9):
                self.weights1[i][j] /= sum

        for i in range(9):
            sum = 0
            for j in range(9):
                sum += abs(self.weights2[i][j])
            for j in range(9):
                self.weights2[i][j] /= sum

    def reset(self):
        randWeight = random.randint(1, 2)
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        if randWeight == 1:
            self.weights1[x][y] = random.uniform(-0.5, 0.5)
        else:
            self.weights2[x][y] = random.uniform(-0.5, 0.5)

    def delete(self):
        randWeight = random.randint(1, 2)
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        if randWeight == 1:
            self.weights1[x][y] = 0
        else:
            self.weights2[x][y] = 0

    def change(self):
        randWeight = random.randint(1, 2)
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        a = random.uniform(-0.05, 0.05)
        if randWeight == 1:
            self.weights1[x][y] += a
        else:
            self.weights2[x][y] += a

    def mutation(self, a, b, c):
        for _ in range(a):
            self.delete()
        for _ in range(b):
            self.reset()
        for _ in range(c):
            self.change()
        self.normalisation()

# agent = Agent()
# agent.normalisation()
# agent2 = Agent(agent)
# agent2.mutation(5, 10, 15)
# print(agent2.moveX([1, 0, 0, -1, 1, 0, -1, 0, 0]))
# agent.reset()
