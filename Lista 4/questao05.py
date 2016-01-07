#encoding: utf-8

statement = 'The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'

statement = statement.replace('.', '').replace(',', '').replace(':', '')
statement = statement.lower()
words = statement.split(' ')
python_words = []
count = 0
has_letter = False

for i in words:
	for j in i:
		if j in 'python' and len(i) > 4:
			count += 1
			python_words.append(i)
			break

print python_words
print 'Existem %d palavras que possuem uma das letras python' %count