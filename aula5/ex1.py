nome = str(input("Digite seu nome?: "))
altura = float(input("Sua altura?: "))
idade = int(input("Sua idade? : "))
peso = float(input("Seu peso?: "))

imc = peso / (altura * altura)

print(f"{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}")