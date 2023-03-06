A = [(11, 7), (15, 10), (17, 14)]
B = [(17, 14), (29, 13)]



liste = A+B
intersection = list(set(A) & set(B))
print(intersection)
for i in liste.copy():
    print(i)
    if i in intersection:
        print("hhhh")
        liste.remove(i)


print(liste)