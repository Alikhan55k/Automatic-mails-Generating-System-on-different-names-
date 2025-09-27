
file1=open("C:/Users/IT LAND/Desktop/Ali/Python is my Love/mails/message.txt","r")
file2=open("C:/Users/IT LAND/Desktop/Ali/Python is my Love/mails/names.txt","r")
names_list=file2.read()
names=names_list.split("\n")
print(names)
data=file1.read()
for name in names:
    new_data=data.replace("[name]", name)
    file3=open('C:/Users/IT LAND/Desktop/Ali/Python is my Love/mails/outputs/'+name+'.txt',"w")
    file3.write(new_data)
    file3.close()
file1.close()
file2.close()