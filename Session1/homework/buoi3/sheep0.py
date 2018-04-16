sheeplist = [5, 7, 300, 90, 24, 50, 75]
print ("hello my name is abc and here are my flock hahahah: ")
print (sheeplist)

for i in range (3):
    print ("month", i+1, ":")
    for j in range (len(sheeplist)):
        sheeplist[j] = sheeplist[j] + 50
    print ("One month has passed, now here is my flock", sheeplist)
    print ("Now my biggest sheep has size", max(sheeplist), "let's shear it")
    sheeplist[sheeplist.index(max(sheeplist))] = 8
    print ("After shearing it, here is my flock", sheeplist)

summ = sum (sheeplist)
print ("My flock has size in total:", summ)
money = summ * 2
print ("I would get", money, "$")
