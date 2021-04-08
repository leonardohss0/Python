import math


class Ponto2D:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Coordenada (' + str(self.x) + ',' + str(self.y) + ')'


class Retangulo:
    def __init__(self, ponto1, ponto2):
        self.ponto1 = ponto1
        self.ponto2 = ponto2

        self.width = abs(ponto1.x - ponto2.x)
        self.height = abs(ponto1.y - ponto2.y)

        

    def calcularArea(self):
        resultado = self.width * self.height
        return resultado

    def calcularIntersecao(self, retangulo):
        intersecao = False

        diff_x = min(self.width, retangulo.width) - max(
            self.width, retangulo.width)
        diff_y = min(self.height, retangulo.height) - max(
            self.height, retangulo.height)

        if (diff_x > 0 and diff_y > 0):
            intersecao = True
            return calcularArea()
        else:
            return None
