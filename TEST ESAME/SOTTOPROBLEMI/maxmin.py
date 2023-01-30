def diff_maxmin (lista):
    minimo = lista[0]
    massimo = lista[0]
    for i in range(1,len(lista)):
        if lista[i] >= massimo:
            massimo = lista[i]
        if lista[i] <= minimo:
            minimo = lista[i]
    return massimo-minimo

#print(diff_maxmin([10,15,15,15,17,19,21,27,27,28,28,30,1,-7,-3,100]))