import multiprocessing as mp
import os


def fatorizar(num:int) -> list:
    rv = []
    for i in range(1, num):
        if num % i == 0:
            rv.append(i)
    
    return rv


def main(): 
    with mp.Pool(os.cpu_count()) as pool:
        entrada = [818182, 188172, 727881, 1282881, 288281]
        i = 0
        for resultado in pool.map(fatorizar, entrada):
            print(entrada[i])
            print(str(resultado) + "\n")
            i = i+1

if __name__ =='__main__':
    main()