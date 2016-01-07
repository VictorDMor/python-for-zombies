#encoding: utf-8

days = input('Número de dias: ')
hours = input('Número de horas: ')
minutes = input('Número de minutos: ')
seconds = input('Número de segundos: ')

time_in_seconds = seconds + ((minutes * 60) + (hours * 3600) + (days * (3600*24)))

print 'O tempo em segundos é %d' %time_in_seconds