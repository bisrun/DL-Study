import numpy as np

from perceptron2 import Perceptron2

def run():
    try:
        print('given\n')

        learning_rate = 0.2
        threshold = 10
        weight = np.array([0,1,0.5])
        samples= np.array([ [1,1,2],
                            [1,2,0],
                            [1,3,1],
                            [1,2,3]])
        no_of_inputs = samples.shape[0]
        labels = np.array([1, 1, -1, -1])

        #---------------------------------------

        my_perceptron = Perceptron2(no_of_inputs, threshold, learning_rate)
        tr = my_perceptron.normalize_traindata(samples, labels)
        trinv = np.dot( np.linalg.inv( np.dot( np.transpose(tr), tr )), np.transpose(tr))
        trinv2 = np.linalg.inv(tr)

        print(trinv)
        print(trinv2)
        print("end")

    except KeyboardInterrupt:
        print('\n\rquit')


if __name__ == '__main__':
    run()