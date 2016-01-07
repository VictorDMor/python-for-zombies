#encoding: utf-8

def mdc(a, b):
	if (b == 0):
		return a
	else:
		return mdc(b, a % b)

a = input('Informe o primeiro número: ')
b = input('Informe o segundo número: ')

d = mdc(a, b)

print 'O máximo divisor comum de %d e %d é %d' %(a, b, d)