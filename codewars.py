def two_sort(array):
    l = list(array)
    print(l)
    l.sort()
    print(l)
    print(l[0])
    k = l[0].split(sep="***",maxsplit=1)
    print(k)




two_sort(["bitcoin", "take", "over", "the", "world",
         "maybe", "who", "knows", "perhaps"])