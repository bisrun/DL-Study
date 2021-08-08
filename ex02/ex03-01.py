import numpy as np

from perceptron2 import Perceptron2

def run():
    try:
        print('given\n')

        learning_rate = 0.2
        threshold = 10
        weight = np.array([0,1,0.5])
        samples= np.array([[1,2,1],
                    [1,4,3],
                    [1,3,5],
                    [1,1,3],
                    [1,5,6]])
        no_of_inputs = samples.shape[0]
        labels = np.array([1, 1, 1, -1, -1])

        #---------------------------------------

        my_perceptron = Perceptron2(no_of_inputs, threshold, learning_rate)
        training_inputs = my_perceptron.normalize_traindata(samples, labels)

        my_perceptron.setWeight(weight)
        my_perceptron.train(training_inputs)



    except KeyboardInterrupt:
        print('\n\rquit')


if __name__ == '__main__':
    run()