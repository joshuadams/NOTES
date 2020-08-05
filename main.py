#Strings
words = 'Hello Hello World'

#Prints the words above
print(words)

#Prints the words in uppercase
print(words.upper())

#Prints the words in lowercase
print(words.lower())

#Replaces the ' '(Space), with ''(No space)
print(words.replace(' ', ''))

#Replaces 'Hello' with 'Goodbye'
print(words.replace('Hello', 'Goodbye'))

#Word Count
print(len(words))

q = input('Do you want to play agian? (y/n)')
#This is going to see if your answer starts with a 'y'. it does not have to be uppercase or lower c 
ask = q.upper().startswith('Y')
print(ask)
# 'Y' == q -- > True




