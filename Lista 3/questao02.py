#encoding: utf-8

user = raw_input('Informe o nome de usuário: ')
password = raw_input('Informe a senha: ')
while(user == password):
	print 'A senha não pode ser igual ao nome de usuário!'
	user = raw_input('Informe o nome de usuário: ')
	password = raw_input('Informe a senha: ')