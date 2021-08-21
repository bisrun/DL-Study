import numpy

import ex01
import ex02
import ex03
import ex04
import ex05
import ex06_01
import ex06_ho_kashyap_proc
import ex01
def run():
    try:
        ex01.run()
        print()
        ex02.run()
        print()
        ex03.run()
        print()
        ex04.run()
        print()
        ex05.run()
        print()
        ex06_01.run()
        print()
        ex06_ho_kashyap_proc.run()



    except KeyboardInterrupt:
        print('\n\rquit')


if __name__ == '__main__':
    run()