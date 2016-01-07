#encoding: utf-8

a = input('Informe o lado 1: ')
b = input('Informe o lado 2: ')
c = input('Informe o lado 3: ')

if (a > (b-c) and a < (b+c)) and (b > (a-c) and b < (a+c)) and (c > (a-b) and c < (a+b)):
	if a == b and a == c:
		print 'Trata-se de um triângulo equilátero!'
	elif a == b or a == c or b == c:
		print 'Trata-se de um triângulo isósceles'
	else:
		print 'Trata-se de um triângulo escaleno'
else:
	print 'Não é um triângulo!'