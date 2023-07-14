
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo o objeto...{}".format(self))
        self.numero = numero
        self. titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("O seu saldo é de R${} e o seu limite disponivel é de {}!".format(self.saldo, self.limite))

    def deposita(self, valor):
        self.saldo += valor
        print("O seu novo saldo é de R${}!".format(self.saldo))

    def sacar(self, valor):
        self.saldo -= valor
        print("O seu novo saldo é de R${}!".format(self.saldo))