#Copyright nsov-canetinha Osvaldo Lucas da Silva Figueiredo
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#      
#http://www.apache.org/licenses/LICENSE-2.0

from Caneta import Caneta
from Manutencao import Manutencao

def principal():
    canetinha = Caneta()
    controle = Manutencao()    
    canetinha.inicio()
    while(controle.getRodar()):
        controle.escolha()
        canetinha.acao(controle.getEscolhido())
        controle.sair()
    
if __name__ == '__main__':
    principal()