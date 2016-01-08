#encoding: utf-8

reader = open('phones-questaoE.txt', 'r')
line = reader.readline()
phones = line.split(' ')
count = 0

for i in phones:
	digit_sum = 0
	consecutive = False
	same_digit = False
	for j in range(0, len(str(i))-1):
		if i[j] == i[j+1]:
			consecutive = True
	for j in str(i):
		digit_sum += int(j)
	if str(i)[0] == str(i)[len(str(i))-1]:
		same_digit = True
	if same_digit is False and consecutive is False and digit_sum % 2 == 0:
		count += 1

print count