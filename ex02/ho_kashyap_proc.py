import numpy as np

class ho_kashyap_proc(object):
    def __init__(self, no_of_inputs, threshold=100, learning_rate=0.01):
        self.threshold = threshold
        self.learning_rate = learning_rate


    def predict(self, Y, weight):
        Ya = np.dot(Y, weight)
        checklist= list(filter( lambda x : True if x < 0.01 else False , Ya ))
        if len(checklist) <= 0 :
            return True
        return False

    def train(self, training_inputs, weight, b ):
        for index in range(self.threshold) :
            e = np.dot(training_inputs, weight) - b
            b = b + self.learning_rate * (e + np.abs(e))
            weight = np.dot( np.dot(np.linalg.inv( np.dot(training_inputs.T, training_inputs)), training_inputs.T), b )

            if self.predict( training_inputs, weight ) :
                return weight
        return 0



    def normalize_traindata(self, samples, labels):
        training_inputs = np.zeros((samples.shape[0], samples.shape[1]))
        for index, (input, label) in enumerate( zip(samples, labels)):
            a = input * label
            training_inputs[index] = a

        return training_inputs;