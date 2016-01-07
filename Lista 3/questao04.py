#encoding: utf-8

def fibonacci(n):
	if n <= 0:
		return 0
	elif n < 3:
		return 1
	else:
		i = fibonacci(n-1) + fibonacci(n-2)
		return i

n = input('Informe o número: ')
f = fibonacci(n)
print 'F%d é %d' %(n, f)