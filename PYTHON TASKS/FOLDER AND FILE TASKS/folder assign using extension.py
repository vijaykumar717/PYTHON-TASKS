import os
import shutil
from os import path
import time
starting_time=time.time()
lists=os.listdir('code')

for data in lists:

    ext=(path.splitext(data))[1].strip('.')
    
    if ext=="jpg":
        
        if not os.path.exists('output/'+ext):
            creation='output/'+ext
            os.makedirs(creation)
        print('processing')  
        source='code/'+data
        destin='output/'+ext+'/'+data
        shutil.move(source,destin)
        
    elif ext=='py':
        
        if not os.path.exists('output/'+ext):
            creation='output/'+ext
            os.makedirs(creation)
            
        source='code/'+data
        destin='output/'+ext+'/'+data
        shutil.move(source,destin)

end_time=time.time()
print("execution time=",end_time-starting_time)
##execution time= 0.08730196952819824







##youtube


import os
import time
start=time.time()
def ArrangeFiles(path):
    files=os.listdir(path)
    extension=[]
    for file in files:
        ext=os.path.join(path,os.path.splitext(file)[1][1:])

        if ext not in extension:
            extension.append(ext)
    for folder in extension:
        try:
            os.mkdir(folder)
        except: pass
        for file in files:
            if os.path.split(folder)[1]==os.path.splitext(file)[1][1:]:
                os.rename(os.path.join(path,file),os.path.join(folder,file))
path=r"C:\python\code"
ArrangeFiles(path)
end=time.time()
exe_time=end-start
print("execution time:",exe_time)


