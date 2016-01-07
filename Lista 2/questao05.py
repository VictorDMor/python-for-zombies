#encoding: utf-8

a = input('Informe o primeiro número: ')
b = input('Informe o segundo número: ')
c = input('Informe o terceiro número: ')
maior = 0
menor = 0

if a > b and a > c:
	maior = a
elif b > a and b > c:
	maior = b
else:
	maior = c

if a < b and a < c:
	menor = a
elif b < a and b < c:
	menor = b
else:
	menor = c

print 'O menor número é %d e o maior número é %d' %(menor, maior)