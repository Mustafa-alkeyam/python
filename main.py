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

people = {'person1':{'name1':'mustafa', 'age1':'22', 'jop1':'developer'},
          'person2':{'name2':'mustafa', 'age2':'22', 'jop2':'developer'},
          'person3':{'name3':'mustafa', 'age3':'22', 'jop3':'developer'}}  
for i,r in people.items():
    print(f"{i}:")
    for n,b in r.items():
        print()