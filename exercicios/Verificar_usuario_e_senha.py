
usario = 'Elian Barros'
senha = '0205'

usario_digitado = input('Digite o nome de usuario: ')
senha_digitada = input('Digite sua senha: ')

while usario_digitado != usario or senha_digitada != senha:
    print('\033[31mNome de Usuario ou Senha incorreto(s)\033[m')
    usario_digitado = input('Digite o nome de usuario: ')
    senha_digitada = input('Digite sua senha: ')

print('\033[32mEntrando...\033[m')