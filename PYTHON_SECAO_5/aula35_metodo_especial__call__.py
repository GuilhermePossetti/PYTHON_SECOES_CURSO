# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable"

class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'Está chamando', self.phone)
        return 12154
call1 = CallMe('44999823540')
retorno = call1('Gui PO7')
print(retorno)