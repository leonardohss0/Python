from Classes import (
    ContaCorrente,
    ContaPoupanca,
)

contacorrente = ContaCorrente()
contapoupanca = ContaPoupanca(contacorrente)
contacorrente.depositar()
contapoupanca.depositar()
contacorrente.sacar()
contapoupanca.sacar()
print(contacorrente)
print(contapoupanca)

"""
while True:
    print(
        "Digite 1 para criar conta corrente\n"
        "Digite 2 para criar conta poupanca\n"
        "Digite 3 para depositar na conta corrente\n"
        "Digite 4 para depositar na conta poupanca\n"
        "Digite 5 para sacar da conta corrente\n"
        "Digite 6 para sacar da conta poupanca\n"
        "Digite 7 para sair"
    )

    a = input()
         

    if(a<=0 or a>7):
        print switch_case.get(number, "Numero invalido")
        break

    def switch_case(number):
        switcher = {
            1: contacorrente = ContaCorrente(),
            2: contapoupanca = ContaPoupanca(),
            3: contacorrente.depositar(),
            4: contapoupanca.depositar(),
            5: contacorrente.sacar(),
            6: contapoupanca.sacar(),
            7: break
        }
"""