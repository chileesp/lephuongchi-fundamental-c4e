print ("hello my name is abc and here are my ship sizes hahahah: ")
sheeplist = [5, 7, 300, 90, 24, 50, 75]
print (sheeplist, sep=", ")

biggest = max(sheeplist)
print ("Now my biggest ship has size", biggest, "let's shear it")

sheeplist[2] = 8
print ("After shearing,here is my flock", sheeplist)

for i in range (len(sheeplist)):
    sheeplist[i] = sheeplist[i] + 50
print ("One month has passed, now here is my flock", sheeplist)
