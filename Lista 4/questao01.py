#encoding: utf-8
from random import randint

numbers = []
higher = 0
lower = 10*3

for i in range(0, 10):
	n = randint(1, 100)
	numbers.append(n)
	if n > higher:
		higher = n
	if n < lower:
		lower = n

print numbers
print 'O maior número é', higher
print 'O menor número é', lower