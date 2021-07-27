#slicing means diving strings. that means creating a substring from extracting elements from another string 
# it has two types that are indexing[] and slice()
#[start:stop:step]

name = "Black storm"
first_name = name[:5]
middle_name = name[5:6]
last_name = name[6:11]

print (first_name)
print(middle_name)
print(last_name)

#the above one is ex for indexing 

#slicing means also extracting req strings from a total string for ex.....

website1 = "www.google.com"

slice = slice(4,-4)

print (website1[slice])