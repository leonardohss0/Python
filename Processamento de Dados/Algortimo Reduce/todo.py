from collections import Counter

import functools
import os
import glob


def conta_um_arquivo(fpath):
    with open(fpath) as input_file:
        cnt = Counter()
        for line in input_file:
            #tornar as palavras minúsculas e tirar \n
            line = line.lower().strip()
            #verificar se ficou linha em branco
            if line:
                #separar cada palavra da lista
                palavras = line.split()
                cnt.update(palavras)
        return cnt


def reduz(contagens_1, contagens_2):
    if contagens_1 != None:
        contagens_1.update(contagens_2.elements())
    return contagens_1


def main():
    pathnames = glob.glob('*.txt')
    final_counting = conta_um_arquivo(pathnames[0])
    for pathname in pathnames[1:]:
        temp_counting = conta_um_arquivo(pathname)
        reduz(final_counting, temp_counting)
    return final_counting.most_common(5)


if __name__ == '__main__':
    main()