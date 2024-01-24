'''f = open("e.txt", "w")

print(f.read())'''



'''f = open("e.txt", "r")

print(f.read(5))'''



'''f = open("sample.txt", "w")
f.write("sachin was born in mumbai.sachin doing good cricket.sachin was failed in 10th std\n")
f.close()

f=open("sample.txt","r").read().split('.')'''       ##words=split()must   ##character= split() no need
    

'''f = open("sachin.txt", "w")
f.write("sachin was born in mumbai.sachin doing good cricket.sachin was failed in 10th std\n")
f.close()

f=open("sachin.txt","r").read().split('.')
output=[]
for a,i in enumerate(f):
    if a!=0:
        i=i.replace('sachin','.he')       ##enumerate keyword
        output.append(i)
    else:
        output.append(i)
print(output)
f=open("sachin.txt","w")
for i in output:
    f.write(i)
f.close()'''

        

'''a=[1,2,3,4,5,'arun']
if  'arun' in a:
    print('crct')
else:
    print('wrong')'''



'''for i in range(1,20):
    if i<10:
        print(i)
        break'''


'''for i in range(1,20):
    if i==10:
        pass
    print(i)'''

'''for i in range(1,20):
    if i==10:
        continue
    print(i)'''




