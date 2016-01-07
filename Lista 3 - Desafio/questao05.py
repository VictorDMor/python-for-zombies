#encoding: utf-8

n = input('Informe o número: ')
reverse = ''

while(n < 0):
	print 'Não é um inteiro positivo!'
	n = input('Informe o número: ')

n = str(n)
for i in range(0, len(n)):
	reverse += n[len(n)-(i+1)]

print reverse