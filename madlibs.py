import re

# open and read the MYDATA file
myFile = open('mydata', 'r')
content = myFile.read()
myFile.close()
print(content)

# search a particular word in sentence
regex = re.compile('NOUN|VERB|ADVERB|ADJECTIVE')
mo = regex.findall(content)

# for each founded word replace it by new word
for x in mo:
    sub = input('Type a ' + x + ': ')
    content = content.replace(x, sub)

# print w new string
print(content)