#encoding: utf-8

a = 80000
b = 200000
i = 0

while(a <= b):
	a = a + (a * 0.03)
	b = b + (b * 0.015)
	i += 1

print 'Levou %d anos para a população de A ser maior que a população de B' %i