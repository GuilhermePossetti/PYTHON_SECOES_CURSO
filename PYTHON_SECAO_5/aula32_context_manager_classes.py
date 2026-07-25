""" Context Manager com classes
Você pode implementar seus próprios protocolos
apenas implementando os dunder methods que o Python vai usar
Isso é chamado de Duck typing onde o Python não astá interessado no tipo,
mas se alguns métodos existem no seu objeto para que ele funcione
de forma adequada DUCK TYPING:
Quando vejo um pássaro que caminha como um pato, nada com um pato
e grasna como um pato, eu chamo aquele pássaro de pato
Para criar um context manager, os métodos __enter__ e __exit__
devem ser implementados o método __exit__ receberá a classe de exceção, a exceção e 
traceback. Se ele retornar True, exceção no with será suprimidas
"""
# with open('aula31_context_manager_classes.txt', 'w') as arquivo:

class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self.arquivo = None

    def __enter__(self):
        print('Abrindo arquivo')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo
    def __exit__(self, class_exception, exception_, traceback_):
        print('Fechando arquivo')
        self._arquivo.close()

with MyOpen('aula31_context_manager_classes.txt', 'w') as arquivo:
    arquivo.write('Linha1\n')
    arquivo.write('Linha2\n')
    arquivo.write('Linha3\n')
    arquivo.write('Linha4\n')
    print('WHIH', arquivo)