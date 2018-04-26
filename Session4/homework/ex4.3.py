enter = int(input("nhap so vao day?"))
for j in range (enter):
    for i in range (enter):
        if (i+j) % 2 == 0:
            print (1, end=" ")
        else:
            print (0, end =" ")
    print()
