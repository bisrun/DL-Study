import numpy as np

from perceptron2 import Perceptron2
from ho_kashyap_proc import ho_kashyap_proc as ho
def run():
    try:
        print('given\n')

        learning_rate = 0.9
        threshold = 200
        weight = np.array([1,1,1])
        b = np.array([1,1,1,1])
        samples= np.array([ [1,6,9],
                            [1,5,7],
                            [1,5,9],
                            [1,0,10]])
        no_of_inputs = samples.shape[0]
        labels = np.array([1, 1, -1, -1])

        #---------------------------------------

        my_ho = ho(no_of_inputs, threshold, learning_rate)
        tr = my_ho.normalize_traindata(samples, labels)

        weight = my_ho.train(tr,weight, b )

        print(weight)

        print("end")

    except KeyboardInterrupt:
        print('\n\rquit')


if __name__ == '__main__':
    run()