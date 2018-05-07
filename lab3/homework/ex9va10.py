def get_even_list(l):
    evenlist = []
    for i in l:
        if i % 2 == 0:
            evenlist.append(i)
    return evenlist

# evenlist = get_even_list([1, 4, 5, -1, 10])
# print('Even list:', evenlist)
even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
