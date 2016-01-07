#encoding: utf-8

n = input('Informe o número: ')
i = 2
p = True

if n <= 2:
	print '%d é primo!' %n
else:
	while (i < n):
		if n % i == 0:
			p = False
			print '%d não é primo!' %n
			break
		i += 1

if p is True and i > 2:
	print '%d é primo!' %n