#encoding: utf-8

salary_hour = input('Informe o salário por hora: ')
hours = input('Informe o número de horas trabalhadas no mês: ')

bruto = salary_hour * hours
ir_deduction = bruto * 0.11
inss_deduction = bruto * 0.08
union_deduction = bruto * 0.05
liquido = bruto - ir_deduction - inss_deduction - union_deduction

print 'Salário Bruto: R$%.2f' %bruto
print 'IR R$%.2f' %ir_deduction
print 'INSS R$%.2f' %inss_deduction
print 'Sindicato: R$%.2f' %union_deduction
print 'Salário Líquido: R$%.2f' %liquido
