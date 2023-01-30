
def sum_csv (file_name):
    my_file = open(file_name, 'r')
    values = []
    for line in my_file:
        elements = line.split(',')
        if elements[0] != 'Date':
            value = elements[1]
            values.append(float(value))
    my_file.close()
    sum = 0
    for item in values:
        sum = sum + item
    return sum
