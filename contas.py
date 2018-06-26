import time
import datetime
class dados: #dados
    def __init__(self): #caracteristicas
        self.nome = ''
        self.idade = 0
        self.altura = 0.00
        self.senha  = ''

    def texto(self):
        self.a = dado.arquivos()
        self.b = open('text.txt','a')
        print(self.a[0],self.a[1],self.a[2],self.a[3],file= self.b)
        self.b.close()
    def arquivos(self):
        return dado.armazenamento(dado.nome, dado.idade, dado.altura,dado.senha)
    def armazenamento(self,nome,idade,altura,senha):#cria uma array
        self.matriz = [nome,idade,altura,senha]
        return self.matriz
dado = dados()
class executa:
    def comeca(self):
        while True:
            print('Para acessar as informações "Digite 3"')
            print('Para ler as nomes já registradas "Digite 2"\nPara Criar um novo cadastro"Digite 1"\ncaso deseje sair "Digite 0"')
            self.decisao = int(input())
            if not (self.decisao == 1 or self.decisao == 0 or self.decisao == 2 or self.decisao == 3):
                self.decisao = rodar.input_errado()
            if self.decisao == 0:
                break
            elif self.decisao ==2:
                rodar.ler_information()
                time.sleep(5)
            elif self.decisao == 1:
                criar()
            elif self.decisao == 3:
                rodar.conta()
                time.sleep(5)


    def input_errado(self):
        while True:
            self.decisao = int(input('Número inserido errado,Digite Novamente:'))
            if self.decisao ==3 or self.decisao ==2 or self.decisao == 1 or self.decisao == 0:
                break
        return self.decisao
    def ler_information(self):
        self.ler = open('text.txt', 'r')
        self.dados = self.ler.read().splitlines()
        self.matriz = []
        for linha in self.dados:
            self.matriz.append(linha.split())
        print('Nomes já registrados:')
        for i in self.matriz:
            print(i[0])
        time.sleep(5)
    def existente(self):
        self.ler1 = open('text.txt', 'r')
        self.dados = self.ler1.read().splitlines()
        self.matriz = []
        for linha in self.dados:
            self.matriz.append(linha.split())
        self.vetor = []
        for i in self.matriz:
            self.vetor.append(i[0])
        self.ler1.close()
        return self.vetor
    def conta(self):
        self.contaa = input('digite o nome da sua conta: ')
        if not(self.contaa in rodar.existente()):
            while True:
                self.contaa = input('Conta não encontrada, digite novamente:')
                if self.contaa in rodar.existente():
                    break
        self.ler_3 = open('text.txt', 'r')
        self.atributos  = self.ler_3.read().splitlines()
        self.contador = 0
        self.matriiz = []
        self.ler_3.close()
        for i in self.atributos:
            self.matriiz.append(i.split())

        for i2 in self.matriiz:
            if self.contaa in i2:
                break
            self.contador+=1
        self.senha_1 = self.matriiz[self.contador][3]
        self.senha_2 = input('Digite sua senha:')

        if self.senha_2 == self.senha_1:
            print('Nome',self.matriiz[self.contador][0])
            print('Idade', self.matriiz[self.contador][1])
            print('Altura', self.matriiz[self.contador][1])
        else:
            print('senha errada')
rodar = executa()
def criar():
    dado.nome = input('digite seu nome:')
    if dado.nome in rodar.existente():
        print('cadastro já existente')
        while True:
            dado.nome = input('digite seu nome novamente:')
            if not(dado.nome in rodar.existente()):
                break
    dado.idade = int(input('digite sua idade: '))
    dado.altura = float(input('digite sua altura: '))
    dado.senha = input('digite a senha:')
    dado.texto()
rodar.comeca()
