import numpy as np

from perceptron2 import Perceptron2

def run():
    try:
        print('given\n')

        learning_rate = 0.2
        threshold = 10
        weight = np.array([0,1,0.5])
        samples= np.array([ [1,6,9],
                            [1,5,7],
                            [1,5,9],
                            [1,0,4]])
        no_of_inputs = samples.shape[0]
        labels = np.array([1, 1, -1, -1])

        #---------------------------------------

        my_perceptron = Perceptron2(no_of_inputs, threshold, learning_rate)
        tr = my_perceptron.normalize_traindata(samples, labels)
        trinv = np.dot( np.linalg.inv( np.dot( np.transpose(tr), tr )), np.transpose(tr))

        print(trinv)
        a2 = np.dot(trinv, np.array([1,1,1,1]))
        print(a2)
        Ya = np.dot(tr, a2)
        print(Ya)
        print("a2 != Ya")

    except KeyboardInterrupt:
        print('\n\rquit')


if __name__ == '__main__':
    run()