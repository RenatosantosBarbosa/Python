nome = str(input("Digite seu nome: "))

qntd_cr = (len(nome))

if qntd_cr <= 4:
    print("Seu nome é curto")
elif qntd_cr >= 5 and qntd_cr <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")