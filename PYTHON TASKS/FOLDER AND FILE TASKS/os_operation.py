'''import os
os.mkdir("c:\\python\\new")
os.getcwd()
os.chdir("vijay")'''#remain syntax utube 
'''import os
os.rename("oldname","new name")
os.remove("folder name")
os.makedirs('basic/code')
os.stat("filename").st_size
print('completed')
list_image=len(os.listdir('basic'))
print(list_image)'''
##import shutil
'''import os'''
##shutil.rmtree('basic')
##shutil.move('a.py','code/b.py')
##shutil.copy('code/b.py','code/c.py')
##shutil.copy('code/c.py','code/d.py')
##shutil.copy('code/d.py','code/e.py')
##shutil.copy('code/e.py','code/f.py')

'''count=(os.listdir('code'))
for i in count:
    shutil.copy('code/'+i,'destination/'+i)'''
'''os.makedirs('basic/code1')
print('completed')'''

'''os.rmdir('code/e.py')'''


'''import os
if not os.path.exists('code'):
    os.mkdir('code')
elif os.path.exists('code'):
    print('folder is already created')'''


'''import os
list=os.listdir('code')
count=1
for data in (list):
    if count%5!=0:
        print(data,count)
    count+=1'''


'''import pathlib
p = pathlib.Path("basic/code")           #for already existing
p.mkdir(parents=True, exist_ok=True)'''


        



import os
from os import path
print(dir(path))



files=os.listdr()
for file in files:
    full_path=path.join(os.getcwd(),file)
    print(path.isdir(full_path))


  print(path.split(full_path)[o])  # display path
  print(path.split(full_path)[1])  # display file
  print(path.splitext(full_path))[1]  # file extension
