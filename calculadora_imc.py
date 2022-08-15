def IMC():

    print("*******************************")
    print("|       Calculadora IMC       |")
    print("*******************************")
    print()

    print("Utilize ( . ) ponto ao invez de ( , ) virgula")
    print()

    altura = float(input("Digite a sua altura: "))
    peso = float(input("Digite seu peso: "))
    imc = peso / (altura**2)
    print()

    if (imc < 17):
        print("************************************************")
        print('Seu IMC é {:.1f}, e está muito abaixo do peso'.format(imc))
        print("************************************************")
    elif (imc < 18.5 and imc >= 17):
        print("************************************************")
        print('Seu IMC é {:.1f}, e está abaixo do peso'.format(imc))
        print("************************************************")
    elif (imc >= 18.5 and imc < 25):
        print("************************************************")
        print('Seu IMC é {:.1f}, e está no peso ideal'.format(imc))
        print("************************************************")
    elif (imc >= 25 and imc < 30):
        print("************************************************")
        print('Seu IMC é {:.1f}, e está com sobrepeso'.format(imc))
        print("************************************************")
    elif (imc >= 30 and imc < 35):
        print("************************************************")
        print('Seu IMC é {:.1f}, e está com obesidade I'.format(imc))
        print("************************************************")
    elif (imc >= 35 and imc < 40):
        print("************************************************")
        print('Seu IMC é {:.1f}, e está com obesidade II'.format(imc))
        print("************************************************")
    else:
        print("************************************************")
        print('Seu IMC é {:.1f}, e está com obesidade III'.format(imc))
        print("************************************************")

if(__name__ == "__main__"):
    IMC()