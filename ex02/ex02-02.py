import numpy as np

def run():
    try:
        print('run\n')
        training_inputs = np.array([[1,1,1,-1,-1],
                   [1,1,1,1,1],
                   [1,-1,-1,-1,1],
                   [1,1,-1,-1,1]])
        labels = np.array([1,-1,-1,1])
        no_of_inputs = 4
        no_of_columne = 5
        normalized_inputs = np.zeros((no_of_inputs, no_of_columne))
        #weights = np.array([0.25,0.25,0.25,0.25,0.25])
        weights = np.array([0.,0.5,0.5,0.,0.])

        #normalized_inputs = np.dot(labels, training_inputs)
        #print(normalized_inputs)



        for index, (input, label) in enumerate( zip(training_inputs, labels)):
            a = input * label
            normalized_inputs[index] = a

        print(normalized_inputs)
        breakable = False
        for _ in range(100):
            mis_count = 0
            for index in range(4) :
                w = weights + normalized_inputs[index]
                v = np.dot(weights, normalized_inputs[index])

                if v < 0 :
                    weights = w
                    mis_count = mis_count + 1;
                if index == 3 and mis_count ==0 :
                    breakable = True
                    break

            if(breakable):
                break
        print("========================")
        print(weights)
        print("that is all")







    except KeyboardInterrupt:
        print('\n\rquit')


if __name__ == '__main__':
    run()