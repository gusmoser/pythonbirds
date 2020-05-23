class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=3):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return  f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe=Pessoa.cumprimentar(self)
        return f'{cumprimentar_da_classe} Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    gustavo = Mutante(nome='Gustavo')
    luciano = Homem(gustavo, nome='Luciano')
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
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(gustavo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(gustavo.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
    pessoa=Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(gustavo, Pessoa))
    print(isinstance(gustavo, Homem))
    print(gustavo.olhos)



