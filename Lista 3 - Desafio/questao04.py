#encoding: utf-8

n = input('Informe o número: ')
div = []
d = 2

while n > 1:
	if n % d == 0:
		n = n / d
		div.append(d)
	else:
		d += 1

print divisores