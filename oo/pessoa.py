class Pessoa:
    olhos = 2 #atributo classe defoult(padrao) comunm a todos da classe pessoa 2 olhos
    def __init__(self, *filhos,nome=None,idade=35):
        self.idade = idade
        self.nome = nome #atributo de instancia
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola, meu nome é {self.nome}'

    @staticmethod         #decoretor
    def metodo_estatico():
        return 42

    @classmethod         #decoretor acessar aclasse q esta execuntando metodo
    def nome_e_atributos_de_classe(cls): # cls faz aluzao a classe Pessoa
        return f'{cls} - olhos {cls.olhos}'



class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe=super().cumprimentar()
        return f'{cumprimentar_da_classe}.aperto de mao'

class Mutante(Pessoa):
    olhos =3

if __name__=='__main__':
    renzo = Mutante(nome='Renzo')
    luciano = Homem(renzo,nome='luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    luciano.olhos=1 # atributos criando dinamicamente atraves da atribuicao
    del luciano.olhos # removido (apaga) o atributo olhos do objeto luciano dianmicamente
    print(renzo.__dict__)
    print(luciano.__dict__)
    #Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos),id(luciano.olhos),id(renzo.olhos))
    print(Pessoa.metodo_estatico(),luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
    pessoa=Pessoa('Anonimo')
    print(isinstance(pessoa,Pessoa))
    print(isinstance(pessoa,Homem))
    print(isinstance(renzo,Pessoa))
    print(isinstance(renzo,Homem))
    print(renzo.olhos)
    print(luciano.cumprimentar())
    print(renzo.cumprimentar())


