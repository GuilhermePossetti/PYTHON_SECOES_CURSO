# desempacotamento em chamadas
# de métados e funções
string = 'ABCD'
lista = ['maria', 'helena', 1, 2, 3, 'eduarda']
tupla = 'python', 'é', 'legal'
salas = [
        #0        1
    ['maria', 'helena', ], # 0
        #0
    ['elaine',], # 1
        #0     1         2
    ['luiz', 'joao', 'eduarda',(0, 10, 20, 30, 40)], # 2
]
print(*salas, sep='\n')#desempacotamento e o sep='\n'serve para separar cada lista uma em baixo da ouitra

p, b, *_, ap, u = lista
print(p, u, ap)

for nome in lista:
    print(nome)