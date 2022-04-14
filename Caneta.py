#Copyright nsov-canetinha Osvaldo Lucas da Silva Figueiredo
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#       
#http://www.apache.org/licenses/LICENSE-2.0

from importlib.util import module_for_loader

class Caneta:

    def __init__(self):
        self.modelo = "Esferografica NACOM genérica"
        self.cor = "Azul"
        self.ponta = 0.5
        self.carga = 100
        self.tampada = True

    def getModelo(self):
        return self.modelo
    def getCor(self):
        return self.cor
    def getPonta(self):
        return self.ponta
    def getCarga(self):
        return self.carga
    def getTampada(self):
        return self.tampada

    def setModelo(self, modificador):
        self.modelo = modificador
    def setCor(self, modificador):
        self.cor = modificador
    def setPonta(self, modificador):
        self.Ponta = modificador
    def setCarga(self, modificador):
        self.carga = modificador
    def setTampada(self, modificador):
        self.tampada = modificador

    def inicio(self):
        print("Classe especial de canetas")
        
    def escrever(self):
        self.funcionalidade("escrever", "escrito", "escrevendo")

    def funcionalidade(self, funcao, funcao2, funcao3):
        print("preparando para ", funcao ,"...")
        print("verificando se há carga...")
        if(self.carga > 10):
            print("carga verificada")
        elif((self.carga < 10) or (self.carga > 0)):
            print("carga verificada")
            print("há pouca carga")
            print("deseja continuar assim mesmo? [s/n]: ")
            ver = input()
            if(ver == "s"):
                print("continuando...")
            elif(ver == "n"):
                print("retornando...")
                return 0 
            else:
                print("opção invalida!")
                print("retornando...")
                return 0 
        else:
            print("não há carga suficiente para executar esta ação")

        z3 = True
        while(z3 == True):
            print("preparando para ", funcao ,"...")
            print("verificando se a caneta está tampada...")
            if(self.tampada == True):
                print("A caneta está tampada, impossível ", funcao)
                x3 = True
                while(x3 == True):
                    print("Deseja destampar a caneta para ", funcao ,"? [s/n]: ")
                    desejo3 = input()
                    if(desejo3 == "s"):
                        print("A caneta está sendo destampada...")
                        self.destampar()
                        print("A caneta foi destampada")
                        x3 = False
                        z3 = True
                    elif(desejo3 == "n"):
                        print("A caneta permanece tampada, nada será ", funcao2 )
                        x3 = False
                        z3 = False
                    else:
                        print("alternativa invalida!")
                        print("Tente novamente")
                        x3 = True
            else:
                print(funcao3 ,"...")
                self.carga = self.carga - 1
                print("Algo foi ", funcao2 ," com sucesso")
                z3 = False

    def rabiscar(self):
        self.funcionalidade("rabiscar", "rabiscado", "rabiscando")

    def pintar(self):
        self.funcionalidade("pintar", "pintado", "pintando")
    
    def tampar(self):
        z1 = True
        while(z1 == True):
            print("Preparando para tampar...")
            print("Verificando se a caneta está tampada...")
            if(self.tampada == True):
                print("A caneta está tampada, impossível tampar novamente")
                x1 = True
                while(x1 == True):
                    print("Deseja destampar a caneta para então tampa-la? [s/n]: ")
                    desejo1 = input()
                    if(desejo1 == "s"):
                        print("A caneta está sendo destampada...")
                        self.destampar()
                        print("A caneta foi destampada")
                        print("Preparando para tampá-la...")
                        x1 = False
                        z1 = True
                    elif(desejo1 == "n"):
                        print("A caneta permanece tampada")
                        x1 = False
                        z1 = False
                    else:
                        print("alternativa invalida!")
                        print("Tente novamente")
                        x1 = True
            else:
                print("tampando...")
                self.tampada = True
                print("A caneta foi tampada com sucesso")
                z1 = False

    def destampar(self):
        z2 = True
        while(z2 ==  True):
            print("Preparando para destamtampar...")
            print("Verificando se a caneta está destampada...")
            if(self.tampada == False):
                print("A caneta está destampada, impossível destampar novamente")
                x2 = True
                while(x2 == True):
                    print("Deseja tampar a caneta para então destampa-la? [s/n]: ")
                    desejo2 = input()
                    if(desejo2 == "s"):
                        print("A caneta está sendo tampada...")
                        self.tampar()
                        print("A caneta foi tampada")
                        print("Preparando para destampá-la...")
                        x2 = False
                        z2 = True
                    elif(desejo2 == "n"):
                        print("A caneta permanece destampada")
                        x2 = False
                        z2 = False
                    else:
                        print("alternativa invalida!")
                        print("Tente novamente")
                        x2 = True
            else:
                print("destampando...")
                self.tampada = False
                print("A caneta foi destampada com sucesso")
                z2 = False

    def acao(self, executado):
        if(executado == "escrever"):
            self.escrever()
        elif(executado == "pintar"):
            self.pintar()
        elif(executado == "rabiscar"):
            self.rabiscar()
        elif(executado == "tampar"):
            self.tampar()
        elif(executado == "destampar"):
            self.destampar()
        elif(executado == "ver modelo"):
            print("modelo: ", self.getModelo())
        elif(executado == "ver cor"):
            print("Cor: ", self.getCor())
        elif(executado == "ver ponta"):
            print("Ponta: ", self.getPonta(), " mm")
        elif(executado == "ver carga"):
            print("Carga: ", self.getCarga(), "%")
        elif(executado == "ver estado da tampa"):
            estado = self.getTampada()
            if(estado):
                print("A caneta está tampada")
            else:
                print("A caneta está destmpada")
        elif(executado == "mudar modelo"):
            print("defina o novo modelo:")
            novom1 = str(input())
            self.setModelo(novom1)
        elif(executado == "mudar cor"):
            print("defina o nova cor:")
            novom2 = str(input())
            self.setCor(novom2)
        elif(executado == "mudar ponta"):
            print("defina a nova ponta:")
            novom3 = float(input())
            self.setPonta(novom3)
        elif(executado == "mudar carga"):
            print("defina a nova carga:")
            novom4 = int(input())
            if(novom4 > 100):
                novom4 = 100
            elif(novom4 < 0):
                novom4 = 0
            self.setCarga(novom4)
        elif(executado == "mudar estado da tampa"):
            print("defina a nova ponta [tampada/destampada]: ")
            novom5 = str(input())
            novoms = True
            while(novoms):
                if(novom5 == "tampada"):
                    novom6 = True
                    novoms = False
                elif(novom5 == "destampada"):
                    novom6 = False
                    novoms = False
                else: 
                    print("Opção invalida!")
                    novoms = True
            self.setTampada(novom6)       
        else:
            print("Erro! Caneta com algum tipo de defeito")


