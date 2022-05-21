class Pessoa:
    olhos = 2 #atributo classe defoult(padrao) comunm a todos da classe pessoa 2 olhos
    def __init__(self, *filhos,nome=None,idade=35):
        self.idade = idade
        self.nome = nome #atributo de instancia
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola {id(self)}'

    @staticmethod         #decoretor
    def metodo_estatico():
        return 42

    @classmethod         #decoretor acessar aclasse q esta execuntando metodo
    def nome_e_atributos_de_classe(cls): # cls faz aluzao a classe Pessoa
        return f'{cls} - olhos {cls.olhos}'

if __name__=='__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo,nome='luciano')
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
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos),id(luciano.olhos),id(renzo.olhos))
    print(Pessoa.metodo_estatico(),luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())



