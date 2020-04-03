
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

