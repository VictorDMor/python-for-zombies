#encoding: utf-8

area = input('Informe a área a ser pintada (em m²): ')
can_number = area / 54

if area % 54 != 0:
	can_number = can_number + 1
	
print 'Você precisará de %d lata(s) de tinta!' %can_number