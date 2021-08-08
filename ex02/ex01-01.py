import numpy as np

from perceptron import Perceptron

def run():
    try:
        print('run\n')
        no_of_inputs = 6
        no_of_columne = 2
        learning_rate = 0.2
        threshold = 100
        weight = np.array([0,1,0.5])
        samples= np.array([[1,1],
                   [2,-2],
                   [-1,-1.5],
                   [-2,-1],[-2,1],[1.5,-0.5]])
        #labels = np.array([1, -1, 1, 1, -1, 1])
        labels = np.array([1, -1, -1, -1, 1, 1])

        norm_labels = np.array([1, 1, 1, 1, 1, 1])

        training_inputs = np.zeros((no_of_inputs, no_of_columne))
        for index, (input, label) in enumerate( zip(samples, labels)):
            a = input * label
            training_inputs[index] = a



        my_perceptron = Perceptron(no_of_inputs,threshold, learning_rate)
        my_perceptron.setWeight(weight)
        my_perceptron.train(training_inputs, norm_labels)



    except KeyboardInterrupt:
        print('\n\rquit')


if __name__ == '__main__':
    run()