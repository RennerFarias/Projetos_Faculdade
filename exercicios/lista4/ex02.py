usuario = input("Digite o usuario: ")
senha = usuario
while usuario == senha:
    senha = input("Digite a senha: ")
    if usuario == senha:
        print("Erro: A senha nao pode ser igual ao usuario")
print("FIM")