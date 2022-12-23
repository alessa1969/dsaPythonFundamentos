''' ***********************************************
*      Data Science Academy - Laboratório 02      *
*                                                 *
* Projeto: Calculadora Aritmética de 4 operações  *
* com entrada e saida pelo console (terminal shell*
* /bash).                                         *
*                                                 *
* Autor : Alexandre Lessa                         *
***************************************************
'''

import os
import time
import sys
os.system('clear')


def imprimeMenuSelecao():
    print('Selecione o número da operação desejada:\n')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair\n')

def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return 'divisão por 0'
    else:
        return num1 / num2




def operador(op, entrada1,entrada2):
    saida = 0
    if op == 1:
        print('\nModo: Soma')
        saida = soma(entrada1, entrada2)
        return print('%r + %r = %r\n ' %(entrada1, entrada2, saida))        
    elif op == 2:
        print('\nModo: Subtração')
        saida = subtracao(entrada1, entrada2)
        return print('%r - %r = %r\n ' %(entrada1, entrada2, saida))
    elif op == 3:
        print('\nModo: multiplicação')
        saida = multiplicacao(entrada1, entrada2)
        return print('%r * %r = %r\n ' %(entrada1, entrada2, saida))        
    elif op == 4:
        print('\nModo: Divisão')
        saida = divisao(entrada1, entrada2)
        return print('%r / %r = %r\n ' %(entrada1, entrada2, saida))        
    elif op == 5:
        return 'sair'

sair = 0
while sair != 5:
    print('\n**************** Python Calculator ****************\n')
    # Seleciona a operação
    imprimeMenuSelecao()
    opcaoOperacao = int(input('Digite sua opção (1/2/3/4) ou 5 para sair:'))

    if opcaoOperacao == 5:
        break       

    numEntrada1 = int(input('Digite o primeiro número.: '))
    numEntrada2 = int(input('Digite o segundo número..: '))
    
    operador(opcaoOperacao, numEntrada1, numEntrada2)
    input('Pressione qualquer tecla para continuar...')
    os.system('clear')

print('\nObrigado por utilizar a nossa calculadora')
tempo_saida = 10
for i in range(tempo_saida):
    sys.stdout.write("*")
    time.sleep(1)
os.system('clear')
