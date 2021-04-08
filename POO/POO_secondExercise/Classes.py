import random

from Exceptions import (
    Error, )


class ContaCorrente:
    def __init__(self):
        self.numberAcount = random.randint(1000000, 9999999)
        self.saldo = 0

    def __get_acountNumber(self):
        return self.numberAcount

    def __str__(self):
        return ("Numero da conta: " + str(self.numberAcount) + "\n"
                "Saldo disponivel: " + str(self.get_saldo()) + "\n")

    def depositar(self):
        number = input("Quanto deseja depositar?\n")

        if (number > 0):
            self.saldo += number
            print("Deposito de " + str(number) +
                  " reais efetuado com sucesso\n")

    def sacar(self):
        number = input("Quanto deseja sacar?\n")

        if (self.saldo > number):
            self.saldo -= number
            print('Saque de ' + str(number) + ' efetuado com sucesso \n')
        else:
            print("Saldo insuficiente")
            print("Saldo disponivel: " + str(self.get_saldo()) + " reais\n ")

    def get_saldo(self):
        return self.saldo


class ContaPoupanca:
    def __init__(self, contaCorrente):
        self.numberAcount = contaCorrente.numberAcount
        self.variacao = random.randint(10, 70)
        self.saldo = 0

    def __get_acountNumber(self):
        return self.numberAcount

    def __str__(self):
        return ("Numero da conta: " + str(self.numberAcount) + "\n"
                "Variacao: " + str(self.variacao) + "\n"
                "Saldo disponivel: " + str(self.get_saldo()) + "\n")

    def depositar(self):

        number = input("Quanto deseja depositar?\n")

        if (number > 0):
            self.saldo += number
            print("Deposito de " + str(number) +
                  " reais efetuado com sucesso\n")

    def sacar(self):

        number = input("Quanto deseja sacar?\n")

        if (self.saldo > number):
            self.saldo -= number
            print('Saque de ' + str(number) + ' efetuado com sucesso \n')
        else:
            print("Saldo insuficiente")
            print("Saldo disponivel: " + str(self.get_saldo()) + " reais\n ")

    def get_saldo(self):
        return self.saldo