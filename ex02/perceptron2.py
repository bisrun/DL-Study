import numpy as np

class Perceptron2(object):
    def __init__(self, no_of_inputs, threshold=100, learning_rate=0.01):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = np.zeros(no_of_inputs + 1 )

    def setWeight(self, weight):
        self.weights = weight


    def predict(self, inputs):
        summation = np.dot(inputs, self.weights)
        if summation > 0 :
            activation = 1
        else:
            activation = 0
        return activation

    def train(self, training_inputs):
        for _ in range(self.threshold):
            for inputs in training_inputs:
                prediction = self.predict(inputs)
                self.weights += self.learning_rate * (1 - prediction) * inputs

                print ("weight={}", self.weights)

    def normalize_traindata(self, samples, labels):
        training_inputs = np.zeros((samples.shape[0], samples.shape[1]))
        for index, (input, label) in enumerate( zip(samples, labels)):
            a = input * label
            training_inputs[index] = a

        return training_inputs;