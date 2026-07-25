"""PYTHON - FUNÇÕES E DECORATORS
│
├── FUNÇÕES
│   │
│   ├─ O que são
│   │   ├─ blocos reutilizáveis de código
│   │   ├─ executam quando são chamadas
│   │   └─ podem receber parâmetros e retornar valores
│   │
│   ├─ Estrutura
│   │
│   │   def funcao(param):
│   │       codigo
│   │       return valor
│   │
│   └─ Funções são OBJETOS
│       ├─ podem ser guardadas em variáveis
│       ├─ podem ser passadas como argumento
│       └─ podem retornar outras funções
│
├── FUNÇÕES DENTRO DE FUNÇÕES
│   │
│   ├─ uma função pode existir dentro de outra
│   │
│   │   def externa():
│   │       def interna():
│   │           pass
│   │
│   └─ a função interna pode acessar coisas da externa
│
├── VARIÁVEIS LIVRES (FREE VARIABLES)
│   │
│   ├─ são variáveis usadas na função interna
│   └─ mas criadas na função externa
│
│       def externa():
│           x = 10
│
│           def interna():
│               print(x)
│
│       x → variável livre
│
├── CLOSURE
│   │
│   ├─ acontece quando
│   │   ├─ uma função interna
│   │   └─ guarda variáveis da função externa
│   │
│   └─ Python "lembra" dessas variáveis
│
│       def externa():
│           x = 10
│
│           def interna():
│               print(x)
│
│           return interna
│
│       func = externa()
│       func()
│
├── NONLOCAL
│   │
│   ├─ permite modificar variáveis da função externa
│   └─ usado dentro da função interna
│
│       def externa():
│           x = 0
│
│           def interna():
│               nonlocal x
│               x += 1
│               print(x)
│
│
├── DECORATORS
│   │
│   ├─ são funções que modificam outras funções
│   ├─ adicionam comportamento antes/depois
│   └─ usam closures internamente
│
│       def decorator(func):
│
│           def interna(*args, **kwargs):
│               print("antes")
│
│               resultado = func(*args, **kwargs)
│
│               print("depois")
│               return resultado
│
│           return interna
│
│
└── SINTAXE DO DECORATOR
    │
    ├─ forma manual
    │
    │   func = decorator(func)
    │
    └─ forma com @
    
        @decorator
        def func():
            pass
"""