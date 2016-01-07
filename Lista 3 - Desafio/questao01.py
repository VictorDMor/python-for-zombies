#encoding: utf-8

n = input('Informe o número: ')
i = 1
t = False

if n < 6:
	print '%d não é triangular!' %n
else:
	while(i+2 <= n):
		if (i * (i+1) * (i+2)) == n:
			print '%d é triangular: é o produto de %d x %d x %d' %(n, i, i+1, i+2)
			t = True
			break
		i += 1

if t is False and n > 6:
	print '%d não é triangular!' %n

