#condition statement
a=5
'''if a!=7:
    print('hello')
else:
  print('hi')'''
'''if a%7==0:
  print('correct')
else:
  print('wrong')'''

   
'''a=int(input('enter your value:'))
if a<0: 
  print('your number is negative')
elif a==0:
    print('your number is equal')
else:
   print('your number is big')'''



'''a=int(input('enter your value:'))
if a<50: 
  print('your number is negative')
elif a>=50 and a<=100:
    print('your number is equal')
else:
   print('your number is big')'''



'''a='restart'
split=a.split('s')[0]
split1=a.split('s')[1]
print(split)
print(split1)
replace=split.replace('r','$')
print(replace)
concatenate=(replace+'s'+split1)
print(concatenate)'''


'''a='restart'
slicing=a[0]
slice1=a[1:]
replace=slicing.replace('r','$')
concatenate=(replace+slice1)
print(concatenate)'''


'''a=(input('enter your gmail:'))
user_address=a.split('@')[0]
domain_address=a.split('@')[1]
if len(user_address)>8 and domain_address=='gmail.com':
 print('welcome')
else:
    print('bye')'''



'''import random
num=int(input("enter your number:"))

final_output=''

for i in range(num):
    output=''
    for j in range(num):
        random_number=random.randint(65,91)
        output+=(chr(random_number))
    final_output+=output+' '

print(final_output)'''



'''name="python is easy to understand python is a programming language"

list1=[]

name1=name.split(' ')

for i in name1:
    if  i not in list1:
        list1.append(i)
    else:
        a=i
        print(a)'''

'''empty=[]
for i in range(1,3):
    name=input("enter a name:")
    if name not in empty:
        empty.append(name)
        print("welcome",name)
    else:
        print("bye")'''


name="python is a language python is easy"
empty=[]
split=name.split()
for i in split:
    length=(len(i))
    empty.append((length,i))
empty.sort()
print(empty)
print(empty[0][-1])
print(empty[-1][1])

         






