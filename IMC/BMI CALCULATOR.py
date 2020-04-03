print('Programa cálculo do IMC')

import func_imc as f


x = False
valid_peso = False
valid_altura = False
valid_sexo = False

while x == False:
    while valid_sexo == False:       
        sexo = input('Digite o sexo(M/F): ').lower()
        if sexo == 'm' or sexo == 'f':
            valid_sexo = True
            print('\n')
        else:
            print('Dado inválido. Responda com M ou F.')

    while valid_peso == False:        
        peso = input('digite seu peso em kg: ')
        try:
            peso = float(peso)
            if peso <= 0:
                print('O peso deve ser maior que zero.')
            else:
                valid_peso = True
                print('\n')
        except:
            print('Peso inválido. O valor de conter apenas números e os decimais separados por ponto.')
    
    while valid_altura == False:        
        altura = input('digite sua altura em metros: ')
        try:
            altura = float(altura)
            if altura <= 0:
                print('A altura deve ser maior que zero.')
            else:
                valid_altura = True
                print('\n')
        except:
            print('Altura inválida. O valor de conter apenas números e os decimais separados por ponto.')

    v_imc = str(f.valor_imc(peso,altura))
    c_imc = f.class_imc(sexo,peso,altura)
    
    print('O seu IMC é: ',v_imc[0:5])
    print('A sua classificação é: ',c_imc)
    print('\n')
    valid_peso = False
    valid_altura = False
    valid_sexo = False

 
    valid_y =  False
    while valid_y == False:
        y = input('deseja calcular novamente?(s/n) ').lower()
        try:
            y == 's' or y == 'n'
            if y == 's':
                x = False
                print('\n')
                valid_y = True
            elif y =='n':
                x = True
                valid_y = True
            else:
                print('resposta inválida')
        except:
            print('resposta inválida')
        




        

