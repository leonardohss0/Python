from functools import reduce

from todo import *

import glob
import os
import sys

#print(os.cpu_count())


def main():
    pasta = os.path.join('.', 'dados', '*.txt')
    #glob vai listar todos os arquivos da pasta dados
    resultado = reduce(reduz, map(conta_um_arquivo, glob.glob(pasta)))

    for palavra in sys.stdin:
        inps = line.strip().split(" ")
        case = int(inps[0])

        if case == 0:
            resultado = "{}".format(next(iter(resultadomap[0].items())))
            print(resultado)

        elif case == 1:
            resultado = "{}".format(next(iter(resultadomap[3].items())))
            print(resultado)

        elif case == 2:
            resultado = "{}".format(resultadofinal.most_common(5))
            print(resultado)

        elif case == 3:
            resultado = "{}".format(resultadofinal.most_common(10))
            print(resultado)

        else:
            print(None)


if __name__ == '__main__':
    main()