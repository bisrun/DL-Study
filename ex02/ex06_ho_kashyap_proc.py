import numpy as np

from ho_kashyap_proc import ho_kashyap_proc as ho

np.set_printoptions(formatter={'float_kind': lambda x: "{0:0.3f}".format(x)})

def run():
    try:
        print('#ex06-Ho-Kashyap procedure')

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
        weight = my_ho.train(tr, weight, b )
        Ya= np.dot(tr, weight)

        print("a={}, b={}".format(weight, my_ho.b))
        print("Ya={}".format(Ya))

        Ya_negatives = list(filter(lambda x: True if x < 0 else False, Ya))
        # all_positive = all(Ya)
        all_positive = True if len(Ya_negatives) <= 0 else False
        if all_positive:
            print("This solution gives a separating hyperplane since Ya > 0")
        else :
            print("This solution does not give a separating hyperplane since Ya < 0")


    except KeyboardInterrupt:
        print('\n\rquit')


if __name__ == '__main__':
    run()