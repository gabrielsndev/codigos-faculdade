def imc(peso, altura):
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        return 'Magreza'
    elif imc >= 18.5 and imc < 24.9:
        return 'Normal'
    elif imc >= 25 and imc < 29.9:
        return 'Sobrepeso'
    elif imc >= 30 and imc < 34.9:
        return 'Obesidade grau I'
    elif imc >= 35 and imc < 39.9:
        return 'Obesidade grau II (severa)'
    else:
        return 'Obesidade grau III (mórbida)'