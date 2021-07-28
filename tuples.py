#tuples = collection which are orderd and unchangeable..
#          used to group together related data.

student = ("neeli",22,"female")   #computers always starts with zero,so its 0,1,2

print(student.index("female"))    #index() means its in 2 place in student tuple. 
print(student.count("neeli"))     #count() , its i 1st place in student tuple.

for i in student:
    print (i)
    
if "neeli" in student:
    print("gokul@kali_linux")   