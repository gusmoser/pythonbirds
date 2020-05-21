class Pessoa:
    def __init__(self, *filhos, nome=None, idade=39):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    gustavo = Pessoa(nome='Gustavo')
    luciano = Pessoa(gustavo, nome='Luciano')
    p = Pessoa('Luciano')
    print(Pessoa.cumprimentar(p))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    p.nome = 'Gustavo'
    print(p.nome)
    print(p.idade)





