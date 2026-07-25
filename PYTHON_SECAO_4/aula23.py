# Introdução às Generator functions em PY
#generator = (n for n in range(100))

def generator(n=0):
    yield 1
    print('Continuando...')
    yield 2
    print('Mais uma...')
    yield 3
    print('Vou terminar...')
    return 'ACABOU'

gen = generator(n=0)
for n in gen:
    print(n)

#|#|#|#|#|#|#|#|#|#|#||#|#|##||#|#|#|##|#||#|#|#|#|#|#|#|#

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return
gen = generator(maximum=100)
for n in gen:
    print(n)