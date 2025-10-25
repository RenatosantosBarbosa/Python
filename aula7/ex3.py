idade = int(input("Qual a sua idade?: "))

if idade <= 17:
    print("Vc é de Menor")
elif idade > 17 and idade <= 50:
    print("Vc é adulto")
else:
    print("Vc é idoso")
