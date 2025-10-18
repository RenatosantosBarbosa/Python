nome = str(input("Qual o seu nome?: "))
idade = int(input("Qual a sua idade?: "))
altura = float(input("Qual sua altura?: "))
peso = float(input("Qual eu peso?: "))
ano_atual = 2025

ano_nascimento = ano_atual - idade
imc = peso / (altura * altura)

print(f"Olá {nome} você tem {idade} anos sua altura é de {altura} você nasceu em {ano_nascimento} e seu IMC é {imc:.2f} ")

