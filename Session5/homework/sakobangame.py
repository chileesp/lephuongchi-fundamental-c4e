py = 1
px = 1

b = {
    "x" : 2,
    "y" : 2
}
while True:
    for y in range (4):
        # print ("- - - -")
        for x in range (4):
            # print ("-", end="")

            if x == px  and y == py:
                print ("P", end =" ")
            elif x == 2 and y == 2:
                print ("B", end =" ")
            elif x == 3 and y == 1:
                print ("G", end =" ")
            else:
                print ("-", end=" ")

        print ()

    move = input ("your move? (a, s, d, w)").lower()
    if move == "d":
        if py == by and bx == px +1:
            px = bx
            bx +=1
        if px < 3:
            px = px +1
    elif move == "w":
        if py > 0:
            py = py -1
    elif move == "a":
        if px > 0:
            px = px -1
    elif move == "s":
        if py < 3:
            py = py +1
