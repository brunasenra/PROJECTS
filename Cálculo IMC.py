print('Programa cálculo do IMC')

def valor_imc(peso,altura):
    valor_imc = peso/(altura*altura)
    return valor_imc

def class_imc(sexo,peso,altura):
    imc = valor_imc(peso,altura)

    if sexo == 'f':
        if imc <= 19.1:
            return "Abaixo do peso."
        elif 25.8 >= imc and  imc > 19.1:
            return "Peso normal."
        elif 27.3 >= imc and  imc > 25.8:
            return "Marginalmente acima do peso."
        elif 32.3 >= imc and  imc > 27.3:
            return "Acima do peso ideal."
        elif imc > 32.3:
            return "Obeso."
        else:
            return "dados inválidos."

    if sexo == 'm':
        if imc <= 20.7:
            return "Abaixo do peso."
        elif 26.4 >= imc and imc > 20.7:
            return "Peso normal."
        elif 27.8 >= imc and imc > 26.4:
            return "Marginalmente acima do peso."
        elif 31.1 >= imc and imc > 27.8:
            return "Acima do peso ideal."
        elif imc > 31.1:
            return "Obeso."
        else:
            return "dados inválidos."

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

    v_imc = str(valor_imc(peso,altura))
    c_imc = class_imc(sexo,peso,altura)
    
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
        

