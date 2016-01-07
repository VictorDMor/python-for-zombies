#encoding: utf-8

price = input('Qual o preço da mercadoria? ')
discount = input('Qual o desconto? ')

discount_value = price * discount * 0.01
purchase_price = price - discount_value

print 'O desconto será de R$%2.f e o preço a pagar será R$%2.f' %(discount_value, purchase_price)