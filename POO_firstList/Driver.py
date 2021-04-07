from Classes import (
    Ponto2D,
    Retangulo,
)

r1_esq_sup = Ponto2D(-6.5, 5.0)
r1_dir_inf = Ponto2D(-2.0, 2.5)
ret1 = Retangulo(r1_esq_sup, r1_dir_inf)

area1 = ret1.calcularArea()
print("%.2f %.2f %.2f" % (ret1.width, ret1.height, area1))

r2_esq_sup = Ponto2D(2.0, 7.0)
r2_dir_inf = Ponto2D(5.0, 4.0)
ret2 = Retangulo(r2_esq_sup, r2_dir_inf)
area2 = ret2.calcularArea()
print("%.2f %.2f %.2f" % (ret2.width, ret2.height, area2))

intersecao = ret1.calcularIntersecao(ret2)
print(intersecao)
