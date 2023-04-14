print("Efetue seu cadastro:")
usuario=str(input("nome de usuario: "))
senha=str(input("senha:"))
while usuario==senha:
	print("ERRO: Seu nome de usuario e sua senha não podem ser iguais, tente novamente")
	usuario=str(input("usuario: "))
	senha=str(input("senha:"))
else:
	print("cadastrado efetuado com sucesso")