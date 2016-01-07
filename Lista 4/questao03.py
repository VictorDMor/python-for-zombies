#encoding: utf-8

from random import randint

a = []
b = []
c = []

for i in range(0, 10):
	na = randint(1, 100)
	nb = randint(1, 100)
	a.append(na)
	b.append(nb)
	c.append(na)
	c.append(nb)

print a
print b
print c