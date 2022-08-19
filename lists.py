#list
list_1 = [23,1,45]
list_2 = ['apple',1,4.3]
print(list_1,list_2, list_2[0])
list_3 = [45, 'hello', [76,90.1]]
print(list_3)
print(list_3[2])

#operations with lists
print(list_3 * 3)
#print(list_3 + 3) gives error
print(list_3 + list_3) #works as *2

#list using range
list_4 = list(range(1,10,2))
print(list_4)