#encoding: utf-8

statement = 'The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'

statement = statement.replace('.', '').replace(',', '').replace(':', '')
statement = statement.lower()
words = statement.split(' ')
python_words = []

for i in range(0, len(words)):
	if words[i][0] in 'python' or words[i][len(words[i])-1] in 'python':
		python_words.append(words[i])

print python_words