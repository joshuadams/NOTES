#For Loop
for i in range(4):
  print('Hello Cool World!')   
  
#This is a Else/If statement
x = 14
if x == 15:
  print(x) 
elif x ==14:
  print(x)
else:
  print("It's not 15")


#This is a line of code that writes out a dictonary 
book = {
    'homogenous':'of the same kind',
    'escapade' : 'exciting adventure',
    'military' : 'serves our country'
  }
print(book.get('homogenous'))
print(book.get('escapade'))








#STRINGS
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


#CLASSES (Dictionaries)
class Test:
  i = 15
  j = 16

x = Test()
print(x.i, x.j)

#ARRAYS
Ratings = [3.7, 4.8, 5.2, 3.6, 4.9]
#           0     1    2   3    4
print(Ratings)
#Prints out the rating numbered 0
print(Ratings[0])

#Changes Rating 3(3.6) to 3.7
Ratings[3] = 3.7
print(Ratings [0])


#FUCTIONS





