def day_count(timestamp): #definisco una funzione che converta il numero di secondi in giorni. voglio sapere se timestamp appartengono a stesso giorno
    day = int(timestamp/86400) #calcolo l'intero dei giorni passati 
    return (day + 1) #ritorno giorno + 1 così da gestire la mezzanotte e da dare al primo giorno il valore 1 invece che 0 (+ intuitivo)

print(day_count(1554073200))
