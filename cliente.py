class Cliente:
    def __init__(self, nome, ):
        self.nome = nome

    @property
    def get_nome(self):
        return self.nome.title()
