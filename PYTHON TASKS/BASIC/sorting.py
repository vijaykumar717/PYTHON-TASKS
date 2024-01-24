data=['c++','java','python','c']

empty_list=[]

for i in data:
    a=(len(i))
    empty_list.append((a,i))
    
print('before sort',empty_list)

empty_list.sort(reverse=True)
empty_list.sort()

print(empty_list)
