#encoding: utf-8

cigs_day = input('Quantos cigarros são fumados por dia? ')
time_smoking = input('Quantos anos tem que você fuma? ')

total_cigs = cigs_day * time_smoking * 365
minutes_lost = total_cigs * 10
days_lost = minutes_lost / 1440

print 'Você perdeu %.2f dias de vida por causa do cigarro' %days_lost