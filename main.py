# print('hello world')

# #1 string
# name = ''' mustafa 
# ali 
# ahmad'''
# print (name)


# #2 int
# nom =1
# print (nom)


# #3 flote
# nom1 =1.2345678
# print (nom)

# #4 polian


# #5 list
# list1 = [1,3,4,2,4,5,5,6]
# print (list1)

# #6 tuple
# tp = (1,3,3,4,5,6,7,78)
# print (tp)

# #7 dictionary : {key: value}
# parsone = {'name': 'mustafa',
# 'age':'20',
#   'jop': 'devlobar',
#    'skils': ['java','python','html','css']} 
#    print (parsone)



# for with in 
# parsone = {'name': 'mustafa',
# 'age':'20',
# 'jop': 'devlobar',
# 'skils': ['java','python','html','css']} 
# print (parsone)
# for i in parsone:
#     print(i,':',parsone[i] )

# def myfunction():
#     print("hello")
# myfunction()  

# people = {'person1':{'name1':'mustafa', 'age1':'22', 'jop1':'developer'},
#           'person2':{'name2':'ahmad', 'age2':'28', 'jop2':'engener'},
#           'person3':{'name3':'khaled', 'age3':'25', 'jop3':'techer'}}  
# for i,r in people.items():
#     print(f"{i}:")
#     for n,b in r.items():
#         print(f"{n} : {b}")


# whiletest = True
# i = 0
# while whiletest :
#     if i==5:
#         continue
#     i+=1
#     if i==10:
#         print(i)
#         i+=1
#         break

# allperson = []
# person = {}
# print("welcome to uor app")
# while True:
#     print('__'*20)
#     print('1 - create account')
#     print('2 - login')
#     print('3 - exit')
#     choice = input('enter your choice')
#     if choice == '1':

#         name = input('enter the user name :')
#         if allperson != []:
#             isExited = True
#             while isExited:
#                 for i in allperson:
#                     if name == i['name']:
#                         print('this name is already exist')
#                         name = input('enter the user name :')
#                         isExited = True
#                         break
#                     else:
#                         isExited = False
        
#         while True:
#             try:
#                 age = int(input('enter the user age : '))

#                 break
#             except Exception as e:
#                 print(e)
#                 continue


        
#         jop = input('enter the user jop :')
#         skills = []
#         while True:
#             try:
#                 counter2 = int(input('enter the number of skills : '))

#                 break
#             except Exception as e:
#                 print('please enter a valid number')
#                 continue
#         for i in range(counter2):
#             print('enter the skills  ',i + 1,':')
#             skills.append(input())

#         while True:
#             pasword = input('enter the pasword : ')
#             upperChar = False
#             lowerChar = False
#             numberChar = False
#             if len(pasword) >=8:
#                 for i in pasword:
#                     if i.isupper():
#                         upperChar = True
#                     elif i.islower():
#                         lowerChar = True
#                     elif i.isdigit():
#                         numberChar = True
#                 if upperChar and lowerChar and numberChar:
#                     print('the pasword is strong')
#                     break
#                 else:
#                     lis1 = [upperChar,lowerChar,numberChar]
#                     lis2 = ['1 upper char ,','1 lower char ,','1 number char ,']
#                     lis3 = ''
#                     for i in range(len(lis1)):
#                         if not lis1[i]:
#                             lis3+=lis2[i]
#                     print('the pasword must have at least ',lis3)

#             else:
#                 print('the pasword is shorter that 8 char')

#         person={
#             'name' : name,
#             'age' : age,
#             'jop' : jop,
#             'pasword' : pasword,
#             'skills' : skills

#         }
        
#         allperson.append(person)
#         print(allperson)
#         print("you added person successfuly")

#     elif choice == '2':
#         # counter = 1
#         # print("__"*20)

#         # print('all person : ')
#         # for i in allperson:
#         #     print('person ',counter)
#         #     for key in i:
#         #         print('     ',key,':',i[key])
#         #     counter+=1
#         print("__"*20)
#         print('please inter your name and pasword: ')
#         name = input('enter the user name: ')
#         pasword = input('enter the password: ')

#         for i in allperson:
#             if i['name']== name and i['pasword']== pasword:
#                 print('welcome ',name)
#                 break
#         else:
#             print('the name or password is wrong')

#     elif choice == '3':
#         print('thank you for using our app')
#         break
#     elif choice == '4':
#         print(allperson)
#     else:
#         print('wrong choice')




# list1 =['a','s','e','y','j','6','9']
# list1.sort()
# print(list1)
# list1.reverse()
# print(list1.count('9'))
# print(list1.__len__())
# list1.pop(5)

import random

print('welcoe to hangman')
print('---'*20)
wordBox = ['mustafa','hangman','python','developer','games']
randomWord = random.choice(wordBox)

for i in randomWord:
    print('-', end='')
def hungman (wrong):
    if (wrong == 0):
        print('\n+---+')
        print('     |')
        print('     |')
        print('     |')
        print('    ===')
    elif (wrong == 1):
        print('\n+---+')
        print('o    |')
        print('     |')
        print('     |')
        print('    ===')
    elif (wrong == 2):
        print('\n+---+')
        print('o    |')
        print('|    |')
        print('     |')
        print('    ===')
    elif (wrong == 3):
        print('\n+---+')
        print(' o   |')
        print('/|   |')
        print('     |')
        print('    ===')
    elif (wrong == 4):
        print('\n+---+')
        print(' o   |')
        print('/|\  |')
        print('     |')
        print('    ===')
    elif (wrong == 5):
        print('\n+---+')
        print(' o   |')
        print('/|\  |')
        print('/    |')
        print('    ===')
    elif (wrong == 6):
        print('\n+---+')
        print(' o   |')
        print('/|\  |')
        print('/ \  |')
        print('    ===')

def printWord(guessLetters):
    counter = 0
    rightLetters =0
    for char in randomWord:
        if (char in guessLetters):
            print(randomWord[counter], end=' ')
            rightLetters+=1
        else:
            print(' ', end=' ')
        counter+=1
    return rightLetters 

def printLines():
    print('\r')
    for char in randomWord:
        print('\u203E', end=" ")

lengthWord = len(randomWord)
amountOfWrong = 0
guessIndex = 0
letterGuess = []
letterRight = 0 

while(amountOfWrong !=6 and letterRight != lengthWord):
    print('\n letters guessed so far: ')
    for letter in letterGuess:
        print(letter,end=' ')
    
    letterGuessed = input('\n guess aletter: ')
    if(randomWord[guessIndex] == letterGuessed):
        hungman(amountOfWrong)
        guessIndex+=1
        letterGuess.append(letterGuessed)
        letterRight = printWord(letterGuess)
        printLines()

    else:
        amountOfWrong+=1
        letterGuess.append(letterGuessed)

        hungman(amountOfWrong)
        letterRight = printWord(letterGuess)

print('game is over!')


