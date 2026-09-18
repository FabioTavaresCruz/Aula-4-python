nome_digitada = input ("Digite o nome: ")
senha_digitada = input ("Digite sua senha: ")
senha_cadastrada = '123'
nome_cadastrada = 'ana'

while senha_digitada != senha_cadastrada or nome_cadastrada != nome_digitada:
    print ("Nome ou Senha incorreta! Tenta novemente.")
    senha_digitada = input ("Digite sua senha: ")
    nome_cadastrada = input ("Digite o nome: ")

print ("Bem-vindo ao Sistema...")