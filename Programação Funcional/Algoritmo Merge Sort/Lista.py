from Detour import *
from math import sqrt


#dividir listas
def split(L):
    if not L:
        return (None, None)

    if not tail(L):
        return (L, None)
    else:
        H0 = head(L)
        H1 = head(tail(L))
        (T0, T1) = split(tail(tail(L)))
        return ((H0, T0), (H1, T1))


#ordenar listas
def sorted(L):
    if not L:
        return True
    elif not tail(L):
        return True
    else:
        C1 = head(L) <= head(tail(L))
        return C1 and sorted(tail(L))


#juntar listas
def merge(L0, L1):
    if not L0:
        return L1
    if not L1:
        return L0
    else:
        H0 = head(L0)
        T0 = tail(L0)
        H1 = head(L1)
        T1 = tail(L1)
        if H0 < H1:
            return (H0, merge(T0, L1))
        else:
            return (H1, merge(L0, T1))


#merge and sort
def mSort(L):
    if not (L):
        return None
    if not tail(L):
        return L
    else:
        (L0, L1) = split(L)
        return merge(mSort(L0), mSort(L1))


#estrutura mapa
def mapL(L, f):
    if not L:
        return None
    else:
        return (f(head(L)), mapL(tail(L), f))


#filtrar a lista
def filterL(L, f):
    if not L:
        return None
    else:
        T = filter(tail(L), f)
        H = head(L)
        return (H, T) if f(H) else T


#filtrar numeros pares
def filterOdds(L):
    return filterL(L, lambda x: x % 2)


#filtrar str
def filterStrs(L):
    return filterL(L, lambda x: isinstance(x, str))


#verificar se e primo
def prime(a):
    if a < 2:
        return False

    for x in range(2, int(sqrt(a)) + 1):
        if a % x == 0:
            return False

    return True


#filtrar primos
def filterPrimes(L):
    return filterL(L, prime)


#concatenar listas
def appendL(L1, L2):
    if not L1:
        return L2
    else:
        return (head(L1), appendL(tail(L1), L2))


#QuickSort = ordenar lista de ordem ascendente
def qSort(L):
    if not L:
        return None
    else:
        H = head(L)
        T = tail(L)
        Small = qSort(filterL(T, lambda x: x < H))
        Bigs = qSort(filterL(T, lambda x: x >= H))

        return appendL(appendL(Smalls, (H, None)), Bigs)