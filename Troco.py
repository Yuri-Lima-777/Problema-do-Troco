# resolução do problema de troco usando programação dinâmica
import os

def menu():
    troco_valor = int(input('Digite valor de troco: '))
    moedas = [1, 5, 10, 25, 50, 100] # moedas para resolução
    # listas iniciadas em zeros para moedas usadas e a sua quantidade
    moedasUsadas = [0] * (troco_valor + 1)
    moedasQtd = [0] * (troco_valor + 1)

    os.system("clear")
    t = voltaTroco(troco_valor, moedas, moedasQtd, moedasUsadas)
    print('Troco para', troco_valor, '=', t, 'moeda(s)!')
    print('moeda(s) essa(s): ')
    apresentaMoedas(moedasUsadas, troco_valor)

def voltaTroco(troco_valor, moedas, moedasQtd, moedasUsadas):
    # for responsável por percorrer todos os valores de troco, de 0 até troco
    for centavos in range(troco_valor + 1):
        controla_moedas = centavos # responsável por receber o valor atual de troco

        novaMoeda = 1 # menor solução possível para qualquer caso, ou seja, a trivial

        # for responsável por percorrer cada uma das moedas que podem ser solução
        for j in [m for m in moedas if m <= centavos]:
            # if que verifica qual a menor quantidade de moedas que compõem a solução
            if(moedasQtd[centavos - j] + 1 < controla_moedas):
                controla_moedas = moedasQtd[centavos - j] + 1
                novaMoeda = j # j é a moeda atual

        moedasQtd[centavos] = controla_moedas # guarda quantidade de moedas
        moedasUsadas[centavos] = novaMoeda # guarda as moedas usadas

    return moedasQtd[troco_valor]

def apresentaMoedas(moedasUsadas, troco_valor):
   valor = troco_valor # pega o troco solicitado
   while valor > 0:
      moeda = moedasUsadas[valor] # seleciona a moeda da solução
      print(moeda)
      valor -= moeda 

menu()