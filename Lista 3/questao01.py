#encoding: utf-8

nota = input('Informe a nota: ')
while(nota < 0 or nota > 10):
	print 'Nota inválida!'
	nota = input('Informe a nota: ')
