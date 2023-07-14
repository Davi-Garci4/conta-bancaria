
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo o objeto...{}".format(self))
        self.numero = numero
        self. titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("O saldo é de R${} do titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor
        print("O seu novo saldo é de R${}!".format(self.saldo))

    def sacar(self, valor):
        self.saldo -= valor
        print("O seu novo saldo é de R${}!".format(self.saldo))