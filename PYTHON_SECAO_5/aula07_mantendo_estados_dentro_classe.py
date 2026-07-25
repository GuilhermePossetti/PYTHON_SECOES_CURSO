class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} Já está filmando...')
            return
        
        print(f'{self.nome} Está filmando...')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} Não está filmando...')
            return
        
        print(f'{self.nome} Está parando de filmar...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} Não pode fotografar filmando...')
            return
        
        print(f'{self.nome} Está fotografando...')

c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()

print()

c2.filmar()
c2.filmar()
c2.fotografar()
c2.parar_filmar()