'''
sentence = 'I love people. People are great'
words = sentence.split()
print(sentence.swapcase())
print(sentence.title())
print(words)
print('love' in sentence)
print(sentence.isalpha())
print(sentence.isalnum())
print('The slash (\\) allow us \\ to escape the default behavior')
'''

fnam = 'testfname'
lnam = 'testlname'
llang = 'Python'
age = 100
height = 200

formated_string = 'I am {} {}. I teach {}. I am {} years old. I am {} meters tall. '.format(fnam, lnam, llang, age, height)

print(formated_string)
a, b, c, d, e, f = llang #unpacking sequence characters into variables
print(a, b, c, d, e, f)
print(llang[::-1])
print(llang[0:6:2])

