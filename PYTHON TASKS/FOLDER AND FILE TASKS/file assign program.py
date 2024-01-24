import os
import shutil

total_data=len(os.listdir('code'))
number_division=2
number_data=int(total_data/number_division)


for single_division in range(number_division):
    
    folder_name=input('enter your folder name:-->')
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        
    count=1
    
    for data in os.listdir('code'):
        
        if count%number_data!=0:
            if count<=5:
                count+=1
                print('1234567',data)
                shutil.copy('code/'+data,folder_name+'/'+data)
                pass
        else:
            shutil.copy('code/'+data,folder_name+'/'+data)
            break
    print('-------completed')
