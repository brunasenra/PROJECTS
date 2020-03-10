print('fatura de compras')

import numpy as np
import pandas as pd
from datetime import date

repetir = 0
produtos = []
valores = []
total = 0
valid_valor = False
valid_quant = False

while valid_quant == False:
    quant = input('Quantos produtos deseja contabilizar? ')
    try:
        quant = int(quant)

        if quant <= 0:
            print('O número de produtos precisa ser maior do que zero')
        else:
            valid_quant = True
    except:
        print('Formato de peso inválido. Use apenas números inteiros.')

              
while repetir < quant:
    produto = input('escreva o nome do produto: ')
    produtos.append(produto)

    while valid_valor == False:
        valor = input('escreva o valor do produto: R$ ')
        try:
            valor = float(valor)
            valid_valor = True
        except:
            print("Formato de valor inválido. Use apenas números e ponto.")
        valores.append(valor)
        
    total += valor
    valid_valor = False
    repetir = repetir+1


df = pd.DataFrame({'Produtos':produtos,'Valores(R$)':valores})

data_atual = date.today()

print('\nData da compra:',data_atual,'\n')

print(df)

print('\nO total da fatura é: R$',round(total,2))
