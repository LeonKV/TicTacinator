import numpy
import ast
import random
import copy


class Agent:
    count = 0

    def __init__(self, agent = None):
        Agent.count += 1
        self.id = Agent.count
        self.n_1 = 27
        self.p_1 = 30
        self.n_2 = 30
        self.p_2 = 30
        self.n_3 = 30
        self.p_3 = 18
        self.age = 0
        if agent is None:
            ran = random.Random()
            l = []
            for i in range(self.p_1):
                l.append([])
                for j in range(self.n_1):
                    l[i].append(ran.uniform(-1, 1))
            self.weights1 = l.copy()

            l = []
            for i in range(self.p_2):
                l.append([])
                for j in range(self.n_2):
                    l[i].append(ran.uniform(-1, 1))
            self.weights2 = l.copy()

            l = []
            for i in range(self.p_3):
                l.append([])
                for j in range(self.n_3):
                    l[i].append(ran.uniform(-1, 1))
            self.weights3 = l.copy()
            self.normalisation()

        else:
            self.weights1 = copy.deepcopy(agent.weights1)
            self.weights2 = copy.deepcopy(agent.weights2)
            self.weights3 = copy.deepcopy(agent.weights3)

    def move_x(self, input):
        options = numpy.matmul(self.weights1, self.convert_s2t(input))
        options = numpy.matmul(self.weights2, options)
        options = numpy.matmul(self.weights3, options)
        index = 0
        max = -1000

        for i in range(9):
            if input[i] == 0:
                if options[2 * i] > max:
                    max = options[i]
                    index = i
        return index

    def copy(self):
        copy_agent = Agent()
        copy_agent.weights1 = self.weights1.copy()
        copy_agent.weights2 = self.weights2.copy()
        copy_agent.weights3 = self.weights3.copy()
        copy_agent.id = self.id
        return copy_agent

    def move_o(self, input):
        options = numpy.matmul(self.weights1, self.convert_s2t(input))
        options = numpy.matmul(self.weights2, options)
        options = numpy.matmul(self.weights3, options)
        index = 0
        max = -1000

        for i in range(9):
            if input[i] == 0:
                if options[2 * i + 1] > max:
                    max = options[i]
                    index = i
        return index

    def normalisation(self):
        for i in range(self.p_1):
            sum = 0
            for j in range(self.n_1):
                sum += abs(self.weights1[i][j])
            if sum == 0:
                sum = 1
            for j in range(self.n_1):
                self.weights1[i][j] /= sum

        for i in range(self.p_2):
            sum = 0
            for j in range(self.n_2):
                sum += abs(self.weights2[i][j])
            if sum == 0:
                sum = 1
            for j in range(self.n_2):
                self.weights2[i][j] /= sum

        for i in range(self.p_3):
            sum = 0
            for j in range(self.n_3):
                sum += abs(self.weights3[i][j])
            if sum == 0:
                sum = 1
            for j in range(self.n_3):
                self.weights3[i][j] /= sum

    def reset(self):
        randWeight = random.randint(1, 3)
        if randWeight == 1:
            x = random.randint(0, self.p_1 - 1)
            y = random.randint(0, self.n_1 - 1)
            self.weights1[x][y] = random.uniform(-0.5, 0.5)
        elif randWeight == 2:
            x = random.randint(0, self.p_2 - 1)
            y = random.randint(0, self.n_2 - 1)
            self.weights2[x][y] = random.uniform(-0.5, 0.5)
        else:
            x = random.randint(0, self.p_3 - 1)
            y = random.randint(0, self.n_3 - 1)
            self.weights3[x][y] = random.uniform(-0.5, 0.5)

    def delete(self):
        randWeight = random.randint(1, 3)
        if randWeight == 1:
            x = random.randint(0, self.p_1 - 1)
            y = random.randint(0, self.n_1 - 1)
            self.weights1[x][y] = 0
        elif randWeight == 2:
            x = random.randint(0, self.p_2 - 1)
            y = random.randint(0, self.n_2 - 1)
            self.weights2[x][y] = 0
        else:
            x = random.randint(0, self.p_3 - 1)
            y = random.randint(0, self.n_3 - 1)
            self.weights3[x][y] = 0

    def change(self):
        randWeight = random.randint(1, 3)
        a = random.uniform(-0.05, 0.05)
        if randWeight == 1:
            x = random.randint(0, self.p_1 - 1)
            y = random.randint(0, self.n_1 - 1)
            self.weights1[x][y] += a
        if randWeight == 2:
            x = random.randint(0, self.p_2 - 1)
            y = random.randint(0, self.n_2 - 1)
            self.weights2[x][y] += a
        else:
            x = random.randint(0, self.p_3 - 1)
            y = random.randint(0, self.n_3 - 1)
            self.weights3[x][y] += a

    def mutation(self, a, b, c):
        for _ in range(a):
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

    def get_weights(self):
        out = str(self.weights1) + '\n'
        out += str(self.weights2) + '\n'
        out += str(self.weights3)
        return out

    def save_weights(self, file):
        f = open(file, 'w')
        save_data = self.get_weights()
        f.write(save_data)
        f.close()

    def update_skillset(self, file):
        f = open(file, 'r')
        self.weights1 = ast.literal_eval(f.readline())
        self.weights2 = ast.literal_eval(f.readline())
        self.weights3 = ast.literal_eval(f.readline())
        f.close()



# agent = Agent2()
# agent.normalisation()
#print(agent.weights1)
#print(agent.weights2)
# agent2 = Agent2(agent)
# agent2.mutation(5, 10, 15)
#print(numpy.matmul(agent.weights1, [1, 0, 0, 1, 1, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]))
#print(agent.move_max([1, 0, 0, 1, 1, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]))
# agent.reset()
