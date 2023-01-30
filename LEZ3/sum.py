my_file = open ('shampoo_sales.csv', 'r')



def sum_csv (my_file):
    values = []
    for line in my_file:
        elements = line.split(',')
        if elements[0] != 'Date':
            value = float(elements[1])
            values.append(value)
    sum = 0
    for item in values:
        sum = sum + item
    return sum

ris = sum_csv (my_file)
print (ris)

my_file.close() 