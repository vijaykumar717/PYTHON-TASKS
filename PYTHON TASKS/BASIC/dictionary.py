'''input_dict={'name':'vijay','age':20,'location':'sivakasi','num':17}
string_dict={}
int_dict={}
for data in input_dict:                            #key                  
    typ=(type(input_dict[data]))
    if typ==str:                                            
        string_dict.update({data:input_dict[data]})      #value=input_dict[data]
        print('hi')
    else:
        int_dict.update({data:input_dict[data]})
print(string_dict)
print(int_dict)'''



'''dict1={1:"ajay",2:"vijay",3:"zayn"}
dict2={4:"abd"}
dict3={}
print(dict1.keys())
print(dict1.values())
dict1.update(dict2)
print(dict1)
print(dict1[1])
dict1[2]="prakash"
print(dict1)
del dict1
print(dict1)
{}.fromkeys(range(1,5),7)
print(dict3)
dict1.pop(2)
print(dict1)'''

'''dict1={}
dict1['name']="arun"
dict1['age']="20"
print(dict1)'''

'''input_dict={"name":[],"age":[]}
for i in range(1,4):
    name=input("enter your name")
    age=int(input("enter yout age"))
    input_dict['name'].append(name)
    input_dict['age'].append(age)
print(input_dict)'''
    


'''num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
sorted_dict = {x: sorted(y) for x, y in num.items()}
print(sorted_dict)'''

    
'''dict1={}
for i in range(1,16):
    key=i
    value=i**2
    output={key:value}
    dict1.update(output)
print(dict1)'''



'''b="he was great"
c={}
for i in b:
    
    if i in c:

        c[i]+=1
    else:
        print(c[i])


print(c)'''









    

