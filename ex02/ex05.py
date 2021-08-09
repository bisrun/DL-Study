import numpy as np

from perceptron2 import Perceptron2

def run():
    try:
        print('#ex05')

        learning_rate = 0.2
        threshold = 10
        weight = np.array([0,1,0.5])
        samples= np.array([ [1,6,9],
                            [1,5,7],
                            [1,5,9],
                            [1,0,4]])
        no_of_inputs = samples.shape[0]
        labels = np.array([1, 1, -1, -1])
        b = np.array([1,1,1,1])
        #---------------------------------------

        my_perceptron = Perceptron2(no_of_inputs, threshold, learning_rate)
        tr = my_perceptron.normalize_traindata(samples, labels)
        trinv = np.dot( np.linalg.inv( np.dot( np.transpose(tr), tr )), np.transpose(tr))

        a = np.dot(trinv, b)
        Ya = np.dot(tr, a)

        print("a={}".format(a))
        print("Ya={} , b={}".format(Ya, b))
        print("ie. Ya != b")

        Ya_negatives = list(filter(lambda x : True if x < 0 else False , Ya ))
        #all_positive = all(Ya)
        all_positive = True if len(Ya_negatives) <= 0 else False
        if all_positive:
            print("This solution gives a separating hyperplane since Ya > 0")
        else :
            print("This solution does not give a separating hyperplane since Ya < 0")

    except KeyboardInterrupt:
        print('\n\rquit')


if __name__ == '__main__':
    run()