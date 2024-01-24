
'''newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)'''
'''empty=["vijay","ajay"]
output=[i.upper() for i in empty]
print(output)'''
'''empty=["Arun","mahesh","vijay","ajay","PRAKASH"]
output=[i  for i in empty if 4<len(empty) and i.isupper()]
print(output)'''
'''output1=[i for i in range(1,101)if i%5==0]
print(output1)
print(output2)'''


'''output=[[i for i in range(6)]for i in range(4)]
print(output)
output=[i for i in 'vijay']
print(output)
output=["even" if i%2==0 else "odd" for i in range(10)]
print(output)
output=[i for i in range(100) if i%3==0 if i%1==0]     #nested
print(output)
matrix=[[10,20,30],[40,50,60],[70,80,90]]
output=[[i[j] for i in matrix] for j in range(len(matrix))]
print(output)'''


'''output = [int(x) for x in input("enter a num:")for i in range(int(input()))]
print(output)'''
