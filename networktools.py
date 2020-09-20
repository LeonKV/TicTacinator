import numpy as np
import random


class LayerDense:
    def __init__(self, n_inputs, n_neurons):
        self.inputs = n_inputs
        self.neurons = n_neurons
        self.weights = 0.1 * np.random.rand(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.matmul(inputs, self.weights) + self.biases

    def forwardReLU(self, inputs):
        self.forward(inputs)
        self.output = np.maximum(0, self.output)

    def normalisation(self):
        for i in range(self.neurons):
            sum = 0
            for j in range(self.inputs):
                sum += abs(self.weights[j][i])
            if sum == 0:
                sum = 1
            for j in range(self.inputs):
                self.weights[j][i] /= sum

    def random_delete(self):
        randy = random.randint(1, self.inputs + 1)
        if randy <= self.inputs:
            x = random.randint(0, self.inputs - 1)
            y = random.randint(0, self.neurons - 1)
            self.weights[x][y] = 0
        else:
            y = random.randint(0, self.neurons - 1)
            self.biases[0][y] = 0

    def random_reset(self):
        randy = random.randint(1, self.inputs + 1)
        if randy <= self.inputs:
            x = random.randint(0, self.inputs - 1)
            y = random.randint(0, self.neurons - 1)
            self.weights[x][y] = random.uniform(-1, 1)
        else:
            y = random.randint(0, self.neurons - 1)
            self.biases[0][y] = random.uniform(-1, 1)

    def random_change(self):
        a = random.uniform(-0.05, 0.05)
        randy = random.randint(1, self.inputs + 1)
        if randy <= self.inputs:
            x = random.randint(0, self.inputs - 1)
            y = random.randint(0, self.neurons - 1)
            self.weights[x][y] += a
        else:
            y = random.randint(0, self.neurons - 1)
            self.biases[0][y] += a

    def get_weights(self):
        return self.weights

    def get_biases(self):
        return self.biases

    def set_weights(self, matrix):
        self.weights = matrix

    def set_biases(self, vector):
        self.biases = vector