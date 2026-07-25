# dataclasses - O que são data classes?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__(), (entre outros) 
# em classes definidas pelo usuários
# Em resumo: dataclasses sãp syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html 
# Em Python, dataclasses são uma forma mais simples de criar classes 
# que servem principalmente para guardar dados.
 
"""
Use dataclass quando:

✅ a classe guarda dados
✅ você quer menos código repetido
✅ a classe é simples
✅ os atributos são o foco principal

Use classe normal quando:

✅ há muita lógica
✅ controle manual do __init__ é importante
✅ comportamento é mais importante que atributos

Aprenda nesta ordem:

Classe normal
__init__
atributos
métodos
encapsulamento
herança
abstração
depois dataclass

Porque aí você entende O QUE ela automatiza.
"""
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    
    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)

if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'otavio')
    p1.nome_completo = 'Guilherme Posetti'
    print(p1.nome_completo)