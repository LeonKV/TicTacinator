import numpy
import ast
import random
import copy
from networktools import LayerDense


class Agent:
    count = 0

    def __init__(self, agent = None):
        Agent.count += 1
        self.id = Agent.count
        self.score = 0
        self.age = 0
        if agent is None:
            self.layer1 = LayerDense(27, 30)
            self.layer2 = LayerDense(30, 30)
            self.layer3 = LayerDense(30, 18)

        else:
            self.layer1 = copy.deepcopy(agent.layer1)
            self.layer2 = copy.deepcopy(agent.layer2)
            self.layer3 = copy.deepcopy(agent.layer3)

    def move_x(self, input):
        self.layer1.forward(self.convert_s2t(input))
        self.layer2.forward(self.layer1.output)
        self.layer3.forward(self.layer2.output)
        options = self.layer3.output
        index = 0
        max = -1000

        for i in range(9):
            if input[i] == 0:
                if options[0][2 * i] > max:
                    max = options[0][2 * i]
                    index = i
        return index

    def move_o(self, input):
        self.layer1.forward(self.convert_s2t(input))
        self.layer2.forward(self.layer1.output)
        self.layer3.forward(self.layer2.output)
        options = self.layer3.output
        index = 0
        max = -1000

        for i in range(9):
            if input[i] == 0:
                if options[0][2 * i + 1] > max:
                    max = options[0][2 * i + 1]
                    index = i
        return index

    def copy(self):
        copy_agent = Agent()
        copy_agent.layer1 = self.layer1.copy()
        copy_agent.layer2 = self.layer2.copy()
        copy_agent.layer3 = self.layer3.copy()
        copy_agent.id = self.id
        return copy_agent

    def normalisation(self):
        self.layer1.normalisation()
        self.layer2.normalisation()
        self.layer3.normalisation()

    def reset(self):
        rand_layer = random.randint(1, 3)
        if rand_layer == 1:
            self.layer1.random_reset()
        elif rand_layer == 2:
            self.layer2.random_reset()
        else:
            self.layer3.random_reset()

    def delete(self):
        rand_layer = random.randint(1, 3)
        if rand_layer == 1:
            self.layer1.random_delete()
        elif rand_layer == 2:
            self.layer2.random_delete()
        else:
            self.layer3.random_delete()

    def change(self):
        rand_layer = random.randint(1, 3)
        if rand_layer == 1:
            self.layer1.random_change()
        elif rand_layer == 2:
            self.layer2.random_change()
        else:
            self.layer3.random_change()

    def mutation(self, a, b, c):
        for _ in range(a):
            self.delete()
        for _ in range(b):
            self.reset()
        for _ in range(c):
            self.change()
        self.normalisation()

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

    def get_layers(self):
        out = str(self.layer1.get_weights()) + '\n'
        out += str(self.layer1.get_biases()) + '\n'
        out += str(self.layer2.get_weights()) + '\n'
        out += str(self.layer2.get_biases()) + '\n'
        out += str(self.layer3.get_weights()) + '\n'
        out += str(self.layer3.get_biases())
        return out

    def save_setting(self, file):
        f = open(file, 'w')
        save_data = self.get_layers()
        f.write(save_data)
        f.close()

    def update_skillset(self, file):
        f = open(file, 'r')
        self.layer1.set_weights(ast.literal_eval(f.readline()))
        self.layer1.set_biases(ast.literal_eval(f.readline()))
        self.layer2.set_weights(ast.literal_eval(f.readline()))
        self.layer2.set_biases(ast.literal_eval(f.readline()))
        self.layer3.set_weights(ast.literal_eval(f.readline()))
        self.layer3.set_biases(ast.literal_eval(f.readline()))
        f.close()