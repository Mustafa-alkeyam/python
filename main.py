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
#     print('1 - add new person')
#     print('2 - see all person')
#     print('3 - exit')
#     choice = input('enter your choice')
#     if choice == '1':

#         name = input('enter the person name :')
#         age = input('enter the person age :')
#         jop = input('enter the person jop :')
#         person['name'] = name
#         person['age'] = age
#         person['jop'] = jop
#         allperson.append(person)
#         print("you added person successfuly")
#     elif choice == '2':
#         counter = 1
#         print("__"*20)

#         print('all person : ')
#         for i in allperson:
#             print('person ',counter)
#             for key in i:
#                 print('     ', key, ':',i[key])
#             counter+=1

#     elif choice == '3':
#         break
# list1 =['a','s','e','y','j','6','9']
# list1.sort()
# print(list1)
# list1.reverse()
# print(list1.count('9'))
# print(list1.__len__())
# list1.pop(5)



