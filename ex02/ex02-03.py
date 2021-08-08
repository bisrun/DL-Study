import numpy as np
from perceptron2 import Perceptron2
def run():
    try:
        print('run\n')
        samples = np.array([[1,1,1,-1,-1],
                   [1,1,1,1,1],
                   [1,-1,-1,-1,1],
                   [1,1,-1,-1,1]])
        labels = np.array([1,-1,-1,1])
        weight = np.array([0.25,0.25,0.25,0.25,0.25])
        #weight = np.array([0.,0.5,0.5,0.,0.])
        no_of_inputs = samples.shape[0]
        threshold = 10
        learning_rate = 1
        #---------------------------------------

        my_perceptron = Perceptron2(no_of_inputs, threshold, learning_rate)
        training_inputs = my_perceptron.normalize_traindata(samples, labels)

        my_perceptron.setWeight(weight)
        my_perceptron.train(training_inputs)






    except KeyboardInterrupt:
        print('\n\rquit')


if __name__ == '__main__':
    run()