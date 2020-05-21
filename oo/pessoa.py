class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=3):
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
    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(gustavo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(gustavo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(gustavo.olhos))







