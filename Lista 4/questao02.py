#encoding: utf-8

from random import randint

numbers = []
par = []
impar = []

for i in range(0, 20):
	n = randint(1, 100)
	numbers.append(n)
	if n % 2 == 0:
		par.append(n)
	else:
		impar.append(n)

print numbers
print par
print impar