print('Rendimento Escolar')
import numpy as np
import pandas as pd
from datetime import date


print('Antes de começar, você deve ter em mãos:')
print('* Nome do professor(a);')
print('* Nome da disciplina;')
print('* Nome da turma;')
print('* Número total de alunos da turma;')
print('* Peso de cada avaliação (caso todas tenham o mesmo peso, coloque 1 para todas);')
print('* Número total de aulas;')
print('* Nomes dos alunos;')
print('* Notas de todas as avaliações;')
print('* Número de faltas dos alunos;')

repetir = 0
media_turma = [ ]
total = 0
valid_nota = False
valid_peso1 = False
valid_peso2 = False
valid_p1 = False
valid_p2 = False
valid_aulas = False
valid_faltas = False
valid_alunos = False

nomes_alunos = []
p1_alunos = []
p2_alunos = []
nf_alunos = []
assid_alunos = []
result_alunos = []

professor = input('Digite o nome do professor(a): ')
disciplina = input('Digite o nome da disciplina: ')
turma = input('Digite a turma(ex:602): ')

##validação de quantitativo de alunos da turma:
while valid_alunos == False:
    alunos = input('digite o número total de alunos da turma: ')
    try:
        alunos = int(alunos)

        if alunos <= 0:
            print('O peso precisa ser maior do que zero')
        else:
            valid_alunos = True
    except:
        print('Formato de peso inválido. Use apenas números inteiros, sem decimais.')

## validação de dados para o peso da avaliação 1:
while valid_peso1 == False:
    peso1 = input('digite o peso da primeira prova: ')
    try:
        peso1 = float(peso1)

        if peso1 <= 0:
            print('O peso precisa ser maior do que zero')
        else:
            valid_peso1 = True
    except:
        print('Formato de peso inválido. Use apenas números e decimais separados por ponto.')

## validação de dados para o peso da avaliação 2:
while valid_peso2 == False:
    peso2 = input('digite o peso da segunda prova: ')
    try:
        peso2 = float(peso2)

        if peso2 <= 0:
            print('O peso precisa ser maior do que zero')
        else:
            valid_peso2 = True
    except:
        print('Formato de peso inválido. Use apenas números e decimais separados por ponto.')

## validação de dados para o quantitativo de aulas:
while valid_aulas == False:
    aulas = input('digite o número total de aulas: ')
    try:
        aulas = int(aulas)

        if aulas <= 0:
            print('O número de aulas precisa ser maior que 0.')
        else:
            valid_aulas = True
    except:
        print('Formato inválido. Use apenas números inteiros, sem decimais.')


while repetir < alunos:
    nome = input('\ndigite o nome do aluno: ')
    nomes_alunos.append(nome)

## validação de dados para a avaliação 1:
    while valid_p1 == False:
        p1 = input('digite a nota da primeira prova: ')
        try:
            p1 = float(p1)

            if p1 < 0 or p1 > 10:
                print('A nota precisa estar entre 0 e 10.')
            else:
                valid_p1 = True
        except:
            print('Formato inválido. Use apenas números e decimais separados por ponto.')
        p1_alunos.append(p1)
        
## validação de dados para a avaliação 2:    
    while valid_p2 == False:
        p2 = input('digite a nota da segunda prova: ')
        try:
            p2 = float(p2)

            if p2 < 0 or p2 > 10:
                print('A nota precisa estar entre 0 e 10.')
            else:
                valid_p2 = True
        except:
            print('Formato inválido. Use apenas números e decimais separados por ponto.')
        p2_alunos.append(p2)

##validação de dados para o quantitativo de faltas:
    while valid_faltas == False:
        faltas = input('digite o número total de faltas do aluno: ')
        try:
            faltas = int(faltas)

            if faltas < 0 or faltas > aulas:
                print('O número de faltas não pode ser menor que 0 ou maior que o número de aulas.')
            else:
                valid_faltas = True
        except:
            print('Formato inválido. Use apenas números inteiros, sem decimais.')

    media = round((peso1*p1 + peso2*p2)/(peso1+peso2),2)
    assiduidade = round(((aulas-faltas)*100)/aulas,2)

    
    if assiduidade >= 70:
        if media>=7:
            resultado = ('Aluno Aprovado')
            
        elif media <4:
            resultado = ('Aluno Reprovado por média')
            
        else:
            resultado = print('Resultado: Aluno em Recuperação')
            PR = float(input('digite a nota da prova final: '))
            media = float(round((media + PR)/2,2))
            
            if media>=5:
                resultado = ('Aluno Aprovado')
            
            else:
                resultado = ('Aluno Reprovado por média')
            
    elif assiduidade < 70:
        if  media >= 5:
            resultado = ('Aluno Reprovado por faltas')
            
        else:
            resultado = ('Aluno Reprovado por faltas e por média')
            
    else:
        print('dados inválidos')

    nf_alunos.append(media)
    assid_alunos.append(assiduidade)
    result_alunos.append(resultado)
        
    total += media
    valid_nota = False
    valid_peso1 = False
    valid_peso2 = False
    valid_p1 = False
    valid_p2 = False
    valid_aulas = False
    valid_faltas = False
    repetir += 1 

linhas=[]
x=1

while x <= alunos:
    
    linhas.append(x)
    x= x+1

df = pd.DataFrame({'nº_chamada':linhas,
                  'Nome':nomes_alunos,
                  'Prova 1':p1_alunos,
                  'Prova 2':p2_alunos,
                  'Nota Final':nf_alunos,
                  'Assiduidade(%)':assid_alunos,
                  'Resultado':result_alunos})

data_atual = date.today()

print('Professor:',professor)
print('Disciplina:',disciplina)
print('Turma:',turma)
print('Nº de alunos:',alunos)
print('Data:',data_atual)
print('Média da turma: ',round(total/alunos,2))
print(' ')
print(df)

print('fim do programa')

input('Aperte ENTER para sair')
