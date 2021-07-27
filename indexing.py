#indexing = it gives access to a sequence elements [str, sets, lists]

name = "gokulneeli"

if (name[0].islower()):
     name = name.capitalize()
print (name)

print(name.find("l"))

print(name.isalpha())

print(name.index("n"))

print(name.isdecimal())

print(name.encode())

print(name.format())

print(name.casefold())


first_name = name[:5].upper()
last_name = name[5:].upper()

print (first_name)

print (last_name)