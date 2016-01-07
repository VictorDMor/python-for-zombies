#encoding: utf-8

km = input ('Quantos kms foram percorridos? ')
days = input('O aluguel foi de quantas diárias? ')

bill = (60 * days) + (0.15 * km)

print 'O preço final do aluguel será de R$%.2f' %bill