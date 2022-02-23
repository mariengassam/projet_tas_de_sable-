cinema = []
for j in range(5):#grande boucle
    col = []
    for i in range(5):#boucle imbriquée
        col.append(0)
    cinema.append(col)
for col in cinema:
    for elem in col:
        print(elem, end = " ")
    print()