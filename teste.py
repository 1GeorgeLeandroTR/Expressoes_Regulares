class MinhaVariavel5:
    def __init__(self):
        self.dicionario_variavel= {}
    def get_variavel(self,valor):
        return self.dicionario_variavel.get(valor)

    def add_valor(self,string_chave,object_valor):
        self.dicionario_variavel[string_chave] = object_valor


oi = MinhaVariavel5()
oi.add_valor("kkk",121)
oi.add_valor("oi",11111)
print(oi.get_variavel('oi'))
