#list contains more than a number or string with index 0 as starting point
shopping_list = ['mango', 'tomato', 'apple', 'carrot']
print(shopping_list)
print(shopping_list[0])
print(shopping_list[3])
print(shopping_list[0:2]) #ending point number does not include in list prints onlu 0 to n-1


#lists are 'mutable' means you can append , delete, modify

x="banana"
shopping_list.append(x) #or directly shopping_list.append('banana') 
print(shopping_list)

shopping_list[2] = 'cherries' #replacement/update using index
print(shopping_list)
print(len(shopping_list))

del shopping_list[3] #delete shopping index
print(shopping_list)

shopping_list2 = ["butter", "bread", "peanut"]
print(shopping_list + shopping_list2)
print(len(shopping_list + shopping_list2))


print(shopping_list*2)
print(len(shopping_list)) #repeated items are not taken into acc

for items in shopping_list:
    print(items)