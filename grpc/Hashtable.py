SUCESSO = 4
ERRO = 5

class Hashtable:

    def __init__(self) -> None:
        # A gente pode usar o dict do python? deixar temporario pra não perder muito tempo
        self.data = dict()

    def create(self, key: str, value: str) -> None:
        if key in self.data:
            return ERRO

        self.data[key] = value
        return SUCESSO

    def read(self, key: str) -> str:
        if key not in self.data:
            return ERRO

        print(f'READ: {self.data[key]}')

        return self.data[key]

    def update(self, key: str, value: str) -> None:
        if key not in self.data:
            return ERRO

        self.data[key] = value
        return SUCESSO

    def delete(self, key: str) -> None:
        if key not in self.data:
            return ERRO

        # self.data[key] = None
        del self.data[key]
        return SUCESSO
