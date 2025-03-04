''' Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando
 uma mensagemde
 erro e voltando a pedir as informações '''

usuario = input("Digite o usuario: ")
senha = usuario
while usuario == senha:
    senha = input("Digite a senha: ")
    if usuario == senha:
        print("Erro: A senha nao pode ser igual ao usuario")
print("FIM")