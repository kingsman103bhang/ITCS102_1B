for marc in range(1,7,1):
    for h in range(7, marc, -1):
        print(" ", end=" ")
    for g in range(marc,0,-1):
        print(g, end=" ")
    for i in range(2,marc+1,1):
        print(i, end=" ")
    print()