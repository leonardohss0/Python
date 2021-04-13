#filter retorna os elementos que atestam verdadeiro para a função

L0 = [1, 2, 3, 4, 5]

#filtrar números maiores que 2
filter(lambda x: x > 2, L0)

T0 = ("amora", "abacate",\
      "beterraba", "cereja"\
      "damasco", "ervilha")

#filtrar frutas que começam com a letra a
p = lambda x: str(x)[0] == 'a'
L = filter(p, L1)


#Duck typing
def firstC(L, C):
    return filter(lambda x: x[0] == C, L)


#filtrar duplas que tem o primeiro elemento igual a 1
firstC([(1, 2), (2, 1), (1, 3)], 1)
