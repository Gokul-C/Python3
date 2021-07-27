#type casting means chaning one data type value to another type of data type for example : int to float or string to float etc....

#in this there are 2 types one  is temporary and another one is permanant....so lets see temporary first

#Temporary type cast------------>

x = 1 #int 

y = 2.5 #float

z = "3"  #string

print (x)
print (int(y))
print (z)

#now lets see permannant type cast-------------------->

x = 1 #int

y = 2.5  #float

z = "3"  #str

y = int(y)
z = int(z)

print (x)
print (y)
print (z*3)


#now see i have multipled z*3 it gives 9......first its an string then i type casted into  integer.