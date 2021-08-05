import numpy

from perceptron import Perceptron

def run():
    try:
        print('run\n')
        training_inputs = numpy.array([[1,1,1,-1,-1],
                   [1,1,1,1,1],
                   [1,-1,-1,-1,1],
                   [1,1,-1,-1,1]])
        labels = numpy.array([1,-1,-1,1])
        no_of_inputs = 4
        my_perceptron = Perceptron(4)
        my_perceptron.train(training_inputs, labels)



    except KeyboardInterrupt:
        print('\n\rquit')


if __name__ == '__main__':
    run()