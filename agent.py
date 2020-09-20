import numpy
import random
import copy


class Agent:

    def __init__(self, hidden_layers, agent = None):
        self.age = 0
        self.weights = []
        self.size = []

        if agent == None:

            self.n = len(hidden_layers) + 1

            self.initiate_size(hidden_layers)

            ran = random.Random()

            for size in self.size:
                l = []
                for i in range(size[1]):
                    l.append([])
                    for j in range(size[0]):
                        l[i].append(ran.uniform(-1, 1))
                self.weights.append(copy.deepcopy(l))

            self.normalisation()

        else:
            self.n = agent.n
            self.size = copy.deepcopy(agent.size)
            for i in range(agent.n):
                self.weights.append(copy.deepcopy(agent.weights[i]))

    def initiate_size(self, hidden_layers):
        self.size.append([])
        self.size[0].append(27)
        for i in range(len(hidden_layers)):
            self.size[i].append(hidden_layers[i])
            self.size.append([])
            self.size[i + 1].append(hidden_layers[i])
        self.size[len(hidden_layers)].append(18)


    def move_x(self, input):
        options = self.get_options(input)
        index = 0
        max = -1000

        for i in range(9):
            if input[i] == 0:
                if options[2 * i] > max:
                    max = options[2 * i]
                    index = i
        return index

    def copy(self):
        copy_agent = Agent2()
        copy_agent.weights1 = self.weights1.copy()
        copy_agent.weights2 = self.weights2.copy()
        copy_agent.id = self.id
        return copy_agent

    def move_o(self, input):
        options = self.get_options(input)
        index = 0
        max = -1000

        for i in range(9):
            if input[i] == 0:
                if options[2 * i + 1] > max:
                    max = options[2 * i + 1]
                    index = i
        return index

    def get_options(self, input):
        converted_input = self.convert_s2t(input)
        res = converted_input
        for i in range(self.n):
            res = numpy.matmul(self.weights[i], res)
        return res

    def normalisation(self):
        for size in self.size:
            weights = self.weights[self.size.index(size)]
            for i in range(size[1]):
                sum = 0
                for j in range(size[0]):
                    sum += abs(weights[i][j])
                if sum == 0:
                    sum = 1
                for j in range(size[0]):
                    weights[i][j] /= sum
            self.weights[self.size.index(size)] = weights # Vielleicht unnoetig kp verstehe nicht wie Python funktioniert

    def reset(self):
        randWeight = random.randint(0, self.n - 1)
        x = random.randint(0, self.size[randWeight][1] - 1)
        y = random.randint(0, self.size[randWeight][0] - 1)
        self.weights[randWeight][x][y] = random.uniform(-0.5, 0.5)

    def delete(self):
        randWeight = random.randint(0, self.n - 1)
        x = random.randint(0, self.size[randWeight][1] - 1)
        y = random.randint(0, self.size[randWeight][0] - 1)
        self.weights[randWeight][x][y] = 0

    def change(self):
        randWeight = random.randint(0, self.n - 1)
        x = random.randint(0, self.size[randWeight][1] - 1)
        y = random.randint(0, self.size[randWeight][0] - 1)
        self.weights[randWeight][x][y] += random.uniform(-0.05, 0.05)

    def mutation(self, a, b, c):
        # a,b,c gegeben als %-Wert im Bezug auf Anzahl der hidden layer
        for _ in range(int(a)):
            self.delete()
        for _ in range(b):
            self.reset()
        for _ in range(c):
            self.change()
        self.normalisation()

    def convert_d2s(self, v):
        vnew = []
        for i in range(9):
            i *= 2
            if v[i] == 1:
                vnew.append(1)
            elif v[i + 1] == 1:
                vnew.append(-1)
            else:
                vnew.append(0)
        return vnew

    def convert_s2t(self, v):
        vnew = []
        for i in range(9):
            if v[i] == 1:
                vnew.append(1)
                vnew.append(0)
                vnew.append(0)

            if v[i] == -1:
                vnew.append(0)
                vnew.append(1)
                vnew.append(0)
            if v[i] == 0:
                vnew.append(0)
                vnew.append(0)
                vnew.append(1)
        return vnew

agent = Agent([15, 15])
agent.normalisation()
#print(agent.weights1)
#print(agent.weights2)
agent2 = Agent(0, agent)
agent2.mutation(5, 10, 15)
#print(numpy.matmul(agent.weights1, [1, 0, 0, 1, 1, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]))
print(agent.move_x([1, 0, 0, 1, 1, 0, -1, 0, -1]))
# agent.reset()
