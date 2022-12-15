    # type: lists / Placeholders

sen = "Hello %s, you're invited to my birthday!"
print(sen%("James"))
arr = ["Bob", "Jake", "Michelle"]

for i in arr:
    print(sen%(i))

sen = "\nHello %s %s, you're invited to my birthday!!"
print(sen%("Barack", "Obama"))

msg = "\nI am %s and my age is %d."
print(msg%("Lucas" , 19))

shoppingList = "eggs, carrots, milk, cherries, apples"
shoppingList2 = ["eggs", "carrots", "milk", "cherries", "apples"]
print(shoppingList2[2])
shoppingList2[2] = "chocolate"
print(shoppingList2)
