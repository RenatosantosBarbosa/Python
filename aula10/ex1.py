numero = input("Digite um número inteiro: ")

if numero.lstrip("-").isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
else:
    print("Não é um número inteiro.")
