class CestaCompras:
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, item, quantidade):
        self.itens[item] = quantidade

    def relatorio_final(self):
        somatorio = 0.0

        for key, value in self.itens.items():
            somatorio += key.valor * (1 - key.desconto) * value

            formated = "{}, {}, {}\nValor unitario: {:.2f}\nValor total: {:.2f}\nValor com desconto: {:.2f}\n".format(
                key.minhaClasse, key.nome, value, key.valor, key.valor * value,
                key.valor * (1 - key.desconto) * value)
            print(formated + "\n")
        print("Somatorio: " + str(somatorio) + "\n")


class Item:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    @property
    def get_nome(self):
        return self.__nome

    def set_nome(self, value):
        self.__nome = value

    @property
    def get_valor(self):
        return self.__valor

    def set_valor(self, value):
        self.__valor = value


class Livro(Item):
    minhaClasse = "Livro"

    def __init__(self, nome, valor):
        Item.__init__(self, nome, valor)
        self.desconto = 0.03


class Brinquedo(Item):
    minhaClasse = "Brinquedo"

    def __init__(self, nome, valor):
        Item.__init__(self, nome, valor)
        self.desconto = 0.05


class Eletronico(Item):
    minhaClasse = "Eletronico"

    def __init__(self, nome, valor):
        Item.__init__(self, nome, valor)
        self.desconto = 0.08