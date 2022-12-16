# some lists

shoppingList2 = ["eggs", "carrots", "milk", "cherries", "apples"]
array1 = [23, 54, 64]
array2 = [43, 23]
numArray = [36, 75, 10006, 1 , -5]

array3 = array1+array2
print(array3)


    # del
del shoppingList2[4]
print("del funcion: ", shoppingList2)

    # len
print("len funcion: ", len(shoppingList2))

    # min    
print("min funcion", min(numArray))

    # max
print("max funcion",max(numArray))

    # append()
shoppingList2.append("brocolli")
print(shoppingList2)

    # .count()
print(shoppingList2.count("brocolli"))

    # sum()
print( sum(array3) )