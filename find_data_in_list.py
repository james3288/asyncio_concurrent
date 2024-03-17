from datetime import datetime 
import os




print(f'{datetime.now():%B %d, %Y %I:%M %p}')
print(datetime.now())


utang = [1,2,56,7,8,8,99,9,3,333]

names = [{"name": "king"},{"name":"james"},{"name":"uayan"}]


filterName = list(filter(lambda x: x % 2 == 0 ,utang))



filterName2 = []
for x in utang:
    if x % 2 == 0:
        filterName2.append(x)

print(filterName)
print(filterName2)


