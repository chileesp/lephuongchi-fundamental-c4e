from random import choice
listword = ["champion", "hello", "beautiful"]
word = choice(listword)
splitword = list(word)
print (splitword)

loop = True
count = 0
while loop:
    for i in range(len(splitword)):
        randomword = choice(splitword)
        print (randomword, end=" ")
        splitword.remove(randomword)

    print()
    result = input("your answer")
    if result == word:
        print ("you win")
        loop = False
    else:
        count += 1
        print ("you lose")
        if count < 3:
            enter = input("do you want to continue? (y/n)").lower()
            if enter == "n":
                loop = False
            elif enter == "y":
                loop = True

        if count == 3:
            print ("end game")
            loop = False
