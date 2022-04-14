#Copyright nsov-canetinha Osvaldo Lucas da Silva Figueiredo
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#     
#http://www.apache.org/licenses/LICENSE-2.0

class Manutencao:
    def __init__(self):
        self.rodar = True
        self.escolhido = "vazio"

    def getEscolhido(self):
        return self.escolhido
    
    def getRodar(self):
        return self.rodar

    def setEscolhido(self, modificador):
        self.escolhido = modificador
    
    def setRodar(self, modificador):
        self.rodar = modificador

    def sair(self):
        x4 = True
        while(x4):
            print("\n\n\nDeseja sair? [s/n]: ")
            rodar = input()
            if(rodar == "n"):
                self.rodar = True
                x4 = False
            elif(rodar == "s"):
                self.rodar = False
                x4 = False
            else:
                print("Alternativa invlida!")
                print("tente novamente")
                x4 = True

    def escolha(self):
        x5 = True
        while(x5):
            print("Que ação você deseja executar?")
            print("escrever, pintar, rabiscar, tampar, destampar, sair, opções avançadas")
            acao = input()
            if((acao == "escrever") or (acao == "pintar") or (acao == "rabiscar") or (acao == "tampar") or (acao == "destampar") or (acao == "sair")):
                self.escolhido = acao
                x5 = False
            elif(acao == "opções avançadas"):
                print("Menu de opções avançadas")
                print("ver modelo, ver cor, ver ponta, ver carga, ver estado da tampa")
                print("alterar modelo, alterar cor, alterar ponta, alterar carga, mudar estado da tampa")
                acao2 = input()
                if((acao2 == "ver modelo") or (acao2 == "ver cor") or (acao2 == "ver ponta") or (acao2 == "ver carga") or (acao2 == "ver estado da tampa") or (acao2 == "mudar modelo") or (acao2 == "mudar cor") or (acao2 == "mudar ponta") or (acao2 == "mudar carga") or (acao2 == "mudar estado da tampa")):
                    self.escolhido = acao2
                    x5 = False
                else:
                    ("opção invalidade! Tente novamente")
                    x5 = True
            else:
                ("opção invalidade! Tente novamente")
                x5 = True
