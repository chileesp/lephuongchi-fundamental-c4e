#READ
#items = ["t shirt", "sweater"]
# print ("Welcome to our shop, what do you want?")
# print ("Our items: ", end="")
# print (*items, sep=", ")

#CREATE
#items = ["t shirt", "sweater"]
# print ("Welcome to our shop, what do you want? Our items: t shirt, sweater, jeans")
# enter = input("Enter new item:")
# items.append(enter)
# print ("Our items: ", end="")
# print (*items, sep=", ")

# UPDATE
# items = ["t shirt", "sweater", "jeans"]
# print ("Welcome to our shop, what do you want? Our items: t shirt, sweater, jeans")
# position = int(input("Update position?"))
# positiontheomay = position - 1
# newitem = input("New item?")
# items[positiontheomay] = newitem
# # items.insert(position, newitem )
# print ("Our items: ", end="")
# print (*items, sep=", ")

#DELETE
items = ["t shirt", "sweater", "jeans"]
print ("Welcome to our shop, what do you want? Our items: t shirt, sweater, jeans")
delposition = int(input("Delete position?"))
delpositionmay = delposition - 1
items.pop(delpositionmay)
print ("Our items: ", end="")
print (*items, sep=", ")
