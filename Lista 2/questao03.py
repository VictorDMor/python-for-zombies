#encoding: utf-8

fish_weight = input('Informe o peso coletado (kg): ')
fine = 0
weight_difference = 0

if fish_weight > 50:
	weight_difference = fish_weight - 50
	fine = weight_difference * 4

print 'Houve um excesso de %d quilo(s) e a multa ser paga será de R$%d' %(weight_difference, fine)
