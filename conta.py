
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo o objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O seu saldo é de R${} e o seu limite disponivel é de {}!".format(self.__saldo, self.__limite))

    def deposita(self, valor):
        self.__saldo += valor
        print("O seu novo saldo é de R${}!".format(self.__saldo))

    def sacar(self, valor):
        self.__saldo -= valor
        print("O seu novo saldo é de R${}!".format(self.__saldo))