nome = str(input("Qual seu nome?: "))
idade = int(input("Digite sua idade: "))

if idade < 18:
    print(f"Olá {nome} vc é menor de idade!") 
else:
    print(f"Olá {nome} vc é maior de idade!")