file = open('shampoo_sales.csv','r')
lista = []
for line in file:
    lista_support = [line] #creo lista temporanea, ci inserisco la riga
    lista.append(lista_support) #aggiungo la lista temporanea alla lista principale

#for item in lista:
    #print(item)

print(lista)