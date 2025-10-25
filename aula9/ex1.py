senha = input("Digite uma senha: ")

qtd_cr = (len(senha))

if qtd_cr < 6:
    print("Minimo 6 caracteres")
else:
    print("Conta criada com sucesso")
