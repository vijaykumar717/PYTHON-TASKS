##def char_frequency(str1):
##    dict1 = {}
##    for n in str1:
##        keys = dict1.keys()
##        print(keys)
##        print(dict1)
####        print(n)
####        if n in keys:
####            dict1[n] += 1
 ####        else:
####            dict1[n] = 1
####    return dict1
##print(char_frequency('google.com'))











'''def remove_char(str, n):
      first_part = str[:n]
      print(first_part)
      last_part = str[n+1:]
      print(last_part)
      return first_part + last_part
print(remove_char('Python', 0))
##print(remove_char('Python', 3))
##print(remove_char('Python', 5))'''




'''def change_sring(str1):
      print(str1[-1:])
      print(str1[1:-1])
      print(str1[:1])
      return str1[-1:] + str1[1:-1] + str1[:1]
      
print(change_sring('abcd'))
print(change_sring('12345'))'''






'''lists=[1,5,8,16,4,5]
first_element=lists[0]
for total in lists:
    if(total > first_element):
        first_element=total
print(first_element)'''



'''lists=[5,5,8,16,4,5]
first_element=lists[0]
for total in lists:
    if(total < first_element):
        first_element=total
print(first_element)'''





'''a=input("Enter Your Data")
b=a.split(",")
print(b)
c=3
e=[]
for row in b:
    d=len(row)
    print(d)
    if(d>c):
        e.append(row)
print(e)'''



'''c=[]
a=int(input("Enter Your value:-"))
for row in range(1,a):
    b=row*row
    c.append(b)
print(c[5:])'''






'''import time
starting_time=time.time()
for row in range(1,11):
    print(row,"*2=",row*2)
ending_time=time.time()
execution_time=ending_time-starting_time
print("Your Program taking is",execution_time)'''





'''import time
starting_time=time.time()
for row in range(1,11):
    c=row*2
    b="{} * 2= {}".format(row,c)
    print(b)
ending_time=time.time()
execution_time=ending_time-starting_time
print("Your Pogram taking is",execution_time)'''




'''a=['viki','yuvi','mahesh','arun','siva','abi']
output=[]      
for row in range(97,122):
    for col in a:
        b=col[0]
        if(b==chr(row)):
            c=chr(row)+col[1:6]
            output.append(c)
print(output)'''




'''for row in range(49,90):
    print(chr(row))
    print(chr(5))
    print(ord("a"))'''



'''a=['arun','mahesh','viki','shiva']
b=[1,2,3,4]
for (row,col) in zip(a,b):
    print(row,col)'''



'''a=[1,2,3]
for row in a:
    print("emp{}".format(row))'''



'''list1 = ['1','2','3','4']
print(list1[0])
s = "-"
c=s.join(list1)
print(c)'''



'''word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

for row in range(97,122):
    for col in word_list:
        b=col[0]
        if(chr(row)==b):
             
            print(col)'''


'''for row in range(2,11):
    for col in range(1,11):
        output=row*col
        print('{}*{}={}'.format(col,row,output))
    print()'''







'''mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)'''

'''a=[2,4,6,2,8,10]
b=[]
for row in a:
    if row not in b:
        b.append(row)

print(b)'''


'''a=[1,2,3,4,5]
print(a[::-1])'''



'''a=[1, 3, 5, 7, 9, 10]
b=[2, 4, 6, 8]
c=[11,12]

a[:4]=b[-1:]=c
print(a)
print(b)'''







'''a='restart'
b=a[0]
c=a.replace(b,'$')
print(type(c))
d=b+c[1:]
print(d)'''









'''test_str = "GeeksforGeeks"
 

all_freq = {}
 
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
 
# printing result
print(all_freq)'''






'''input_string = input("enter a word:")
mySet = set(input_string)
print(mySet)
for element in mySet:
    countOfChar = 0
    for character in input_string:
        if character == element:
            countOfChar += 1
    print("Count of character '{}' is {}".format(element, countOfChar))'''








'''a='restart'
b=a[0]
c=a.replace(b,'$')
print(type(c))
d=b+c[1:]
print(d)'''





'''a='abc'
b='xyz'
c=b[2:];
e=a[:-1];
output=e+c;
print(output)
f=b[:-1];
g=a[-1];
out=f+g;
print(out)'''





'''a=input('enter Your String')
b=len(a)
c='ing'
d='gly'
if(b<=6):
    if(a[-1]=='g' and a[-2]=='n' and a[-3]=='i'):
        e=a[:-1]
        out=e+d
        print(out)
    else:
        out=a+c
        print(out)'''




'''a=["PHP", "Exercises", "Backend"]
b=[]
for row in a:
    b.append((len(row),row))
b.sort()
print(b)'''



'''a=input("Enter Your String")
b=int(input("Index of String"))
first_part = a[:b] 
last_part = a[b+1:]
print(first_part)
print(last_part)
output=first_part+last_part
print(output)'''



'''a=input("Enter Your Data:-")
b=len(a)
d=''
for row in range(0,b):
    if(row%2==0):
        d=d + a[row]
print(d)'''





'''a='arun was born in sivakasi'

splitting=a.split(' ')
output=''
full_sentence=' ' 

for row in splitting:
    first_char=row[0]
    upper_case=first_char.upper()
    replacing=first_char.replace(first_char,upper_case)
    final=replacing+row[1:]

    output=final+' '
    full_sentence+=output

print(full_sentence)'''



'''new = [12, 35, 9, 56, 24]
get = new[-1], new[0]
print(get)
new[0], new[-1] = get
print(new)'''




'''a=int(input("enter a number"))
b=int(input("enter a number"))
if b==0: a,b=b,a
while b !=0:
        data = a & b
        print(data)
        a = a ^ b
        print(a)
        b = data << 1
        print(b)
        print(a)'''



'''n=int(input("enter a number"))

if n & 1==1:
    print("odd")
else:
    print("even")'''

'''m=int(input("enter a number"))
d=m/2
if d/d==1:
    print("even")
else:
    print("odd")'''

'''a=int(input("enter a number"))
if a/2==a//2:
    print("even")
else:
    print("odd")'''



'''a=int(input("enter a number"))
if type(a/2)==int:
    print("even")
else:
    print("odd")'''


'''a=int(input("enter a number"))
b=a//2
print(b)

if b*2==a:
    print("even")
else:
    print("odd")'''





'''a="vijay kumar"
c=""

for i in a:
    c=i+c
print(c)


dict={}
for i in a:
    if i in dict:
        dict[i]=+1
    else:
        dict[i]=1
print(dict)'''



'''d=[]
for i in range(10,29):
    c=str(i)
    f=c.split()
    if f[0][0]==f[0][1]:
        continue
    else:
        d.append(f)
print(d)'''
    














