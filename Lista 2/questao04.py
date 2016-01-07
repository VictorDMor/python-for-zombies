#encoding: utf-8

a = input('Informe o primeiro número: ')
b = input('Informe o segundo número: ')
c = input('Informe o terceiro número: ')
maior = 0

if a > b and a > c:
	maior = a
elif b > a and b > c:
	maior = b
else:
	maior = c

print 'O maior número é', maior 