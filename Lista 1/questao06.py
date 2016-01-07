#encoding: utf-8

distance = input('Qual será a distância percorrida (km)? ')
avg_speed = input('Qual será a velocidade média esperada para a viagen (km/h)? ')

time = float(distance) / float(avg_speed)

print 'O tempo estimado da viagem será de %.2f horas' %time