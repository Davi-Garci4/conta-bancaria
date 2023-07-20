
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo o objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O seu saldo é de R${} e o seu limite disponivel é de {}!".format(self.__saldo, self.__limite))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):   #Aqui eu estou analisando se o valor a sacar é compatível com o limite total
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def sacar(self, valor):            #Aqui eu estou vericando se o valor é compatível e realizando o saque, e caso não seja imprime a mensagem
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor de {} ultrapassou o limite".format(valor))


    def transferir(self, valor, destino):        #Essa função cria a ação da transferência entre contas
        self.sacar(valor)
        destino.depositar(valor)

    @property            #Aqui eu estou chamando o método para me retornar o saldo
    def saldo(self):
        return self.__saldo

    @property         #Aqui eu estou chamando o método, para me retornar "get" o nome do titular
    def titular(self):
        return self.__titular

    @property         #Aqui eu crio uma estrutura do modo "get" só que com essa propriedade eu consigo utiliza-la de uma maneira mais objetiva
    def limite(self):
        return self.__limite

    @limite.setter          #Aqui eu chamo a propriedade limite e crio o seu "set", também uma maneira mais fácil.
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @staticmethod          #Esse método serve para poder se chamar uma função dentro de uma classe sem necessariamente se ter um parâmetro, porque essa é uma função estática que nunca muda
    def codigo_banco():
        return "001"
