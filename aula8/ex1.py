usuario = input("Digite seu usuario: ")
senha = input("Digite sua senha: ")

usuario_bd = "Alex"
senha_bd = "123456"

if usuario == usuario_bd and senha == senha_bd:
    print("Login bem sucedido")
else:
    print("Usuario ou senha incorreto.")
