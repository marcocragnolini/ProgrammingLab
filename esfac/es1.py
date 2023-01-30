def stampa (lista):
    for item in lista:
        print(item)

def statistiche (lista):
    valori_statistici = []
    somma = 0
    for item in lista:
        if isinstance (item,int):
            somma+=item
        else:
            return valori_statistici
    valori_statistici.append(somma)
    valori_statistici.append(somma/len(lista))
    minimo = lista[0]
    massimo = lista[0]
    for i in range (1,len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
        if lista[i] > massimo:
            massimo = lista[i]
    valori_statistici.append(minimo)
    valori_statistici.append(massimo)
    return(valori_statistici)

valori_statistici = statistiche([3,3,5,7,3,2,6,8,9,4,2,4,7,8])
stampa(valori_statistici)
        
        
            