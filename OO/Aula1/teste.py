
'''
Python 3: Introdução a Orientação a objetos
Atividade - Aula 1 - 19-07-2020
'''

def cria_conta(numero, titular, saldo, limite):
    conta = { "numero": numero, "titular": titular, "saldo":saldo, "limite": limite }
    return conta
def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo {}".format(conta["saldo"]))

