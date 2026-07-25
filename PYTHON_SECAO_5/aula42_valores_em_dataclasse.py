# Valores padrão e field em dataclasses

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str = 'missg' #valor patrão, mas só imutáveis
    sobrenome: str = 'not sent' #valor patrão, mas só imutáveis
    idade: int = 0 #valor patrão, mas só imutáveis


if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'otavio', 30)
    print(p1)