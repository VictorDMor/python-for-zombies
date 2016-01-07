#encoding: utf-8

salary = input('Qual é o salário atual? R$')
raise_perc = input('Qual é o percentual de aumento? ')

new_salary = salary + (salary * raise_perc * 0.01)

print 'O novo salário é %2.f' %new_salary