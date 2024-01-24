'''starting_num=int(input("enter starting value"))
ending_num=int(input("enter ending value"))
for number in range(starting_num,ending_num+1):
    count=0
    for i in range(2,(number\\2+1)):
               if(number%i==0):
                  count+=1
                  break
    if(count==0 and number!=1):
                  print("%d"%number,end='    ')'''


'''n=4
count=0 
for j in range(2,8):
    if(n%j==0 and n not in[2,3,5,7]):
        count=count+1
        break
                
if count==0:
    print(f"{n} is prime")
else:
    print(f"{n} is not a prime")'''


'''for i in range(1,100):
    count=0 
    for j in range(2,8):
        if(i%j==0 and i not in[2,3,5,7]):
            count=count+1
            break
                
    if count==0 and i!=1:
        print(i)'''



'''b=int(input("enter a number"))
flag=False
if b>1:
    for a in range(2,b):
        if(b%a==0):
            flag=True
            break
if flag:
    print(b,"is not a prime number")
else:
    print(b,"is a prime number")'''





'''primenumlist=[]
for iteration in range(3,20):
    flag=False
    for a in range(2,iteration):
        if(iteration%a==0):
            flag=True
            break
        
    if flag==False:
        primenumlist.append(iteration)
        
print(primenumlist)'''




     
   

               
               
