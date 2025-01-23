# slicing = create a sub string by extracting elements from another string 
#           indexing[] or slice()
#           [start:stop:step]

name = "Faith Oladedonye"

first_name = name[5]                   #start
last_name = name[5:8]                  #stop
funky_name = name[::3]                 #step
reversed_name = name[::-1]

#first_name = name[4:]            #[4:end]
#first_name = name[::2]           #[0:end:2]
#first_name = name[::-1]          #[0:end:-1]

#print(first_name)
#print(last_name)
#print(funky_name)
#print(reversed_name)

#SLICING FUNCTION

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])