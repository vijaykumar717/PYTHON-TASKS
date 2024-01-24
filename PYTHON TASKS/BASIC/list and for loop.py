'''bucket=['red','blue','white']
bucket.append('yEllow')
bucket.insert(2,'green')
bucket.pop(0)
bucket.remove('blue')
print(bucket)'''

'''bucket=['red','green','white','black','yellow']
empty_list=[]
for data in bucket:
    if len(data)==5:
     empty_list.append(data)
print(empty_list)'''

'''name=['vijay','ajay','prakash']
empty_list=[]
for data in name:
    if len(data)>=5:
        empty_list.append(data)
print(empty_list)'''

'''name=['viki','aruna','mahesh','mam']
empty_list=[]
for data in name:    #order properly
    first_char=data[0]
    last_char=data[-1]
    print(first_char,data,last_char)
    if first_char==last_char:
        empty_list.append(data)
print(empty_list)'''


'''a=[1,2,3,4,5,6,7,8,9,10]       #order properly
even_list=[]
odd_list=[]
for data in a:
    if data%2==0:
     even_list.append(data)
    elif data%2==1:
     odd_list.append(data)
print(even_list)
print(odd_list)'''


'''five_list=[]
seven_list=[]
num_list=[]
for i in range(1,101):        #more numbers iterate to list 
    num_list.append(i)

for data in num_list:
    if data%5==0:    #and 
        five_list.append(data)
    elif data%7==0:
        seven_list.append(data)

print(five_list)'''



'''bank=input('1.deposit 2.withdraw:-')
main_balance=10000
if bank=='1':
 deposit_amount=int(input('type your amount:'))
 total_balance=main_balance+deposit_amount
 print(total_balance)
else:
 withdraw=int(input('type your needed amount:'))
 if withdraw>=main_balance:
     print('insufficient amount')
 else:
     print(main_balance-withdraw,'take it')'''
 
   

'''name_list=['vijay','ajay']
name_list.sort()
name_list.sort(reverse=true)
print(name_list)
first_list=[1,2,3,4]
second_list=['a','b']
first_list.extend(second_list)
print(first_list)
total=first_list+second_list
print(total)'''

'''a='massv26@gmail.com'
user_address=a.split('@')[0]
domain_address=a.split('@')[1]
upper_count=0
lower_count=0
num_count=0
if domain_address=='gmail.com':
    for i in user_address:
        if i.isupper():
            upper_count+=1
        elif i.islower():
            lower_count+=1
        else:
            num_count+=1
total_count=upper_count+lower_count+num_count
print(lower_count)
print(total_count)
if total_count<=8:
        print('welcome')
else :
    print('valid')'''


'''list1=[1,2,3,4,5,6,7,8,9,10]
list2=[]
for index,value in enumerate(list1):
    if index%2==1:
        list2.append(value)

print(list2)'''



'''list1=[]
range1=int(input("enter your range:"))
for i in range(1,range1+1):
    name=input("enter your name:")
    list1.append(name)
print(list1)'''

 
    




        

