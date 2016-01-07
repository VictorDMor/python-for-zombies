#encoding: utf-8

bill = input('Qual o valor da conta a ser paga? ')
cash = input('Qual o valor do pagamento efetuado? ')
bills = [0, 0, 0, 0, 0, 0]

change = cash - bill

while (change != 0):
	if change >= 50:
		change -= 50
		bills[0] += 1
	elif change >= 20:
		change -= 20
		bills[1] += 1
	elif change >= 10:
		change -= 10
		bills[2] += 1
	elif change >= 5:
		change -= 5
		bills[3] += 1
	elif change >= 2:
		change -= 2
		bills[4] += 1
	else:
		change -= 1
		bills[5] += 1

print 'O troco será em %d notas de 50, %d notas de 20, %d notas de 10' %(bills[0], bills[1], bills[2])
print '%d notas de 5, %d notas de 2 e %d notas de 1' %(bills[3], bills[4], bills[5])