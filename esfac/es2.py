from datetime import datetime

def get_date(file):
    date_list = []
    for line in file:
        cleaned_line = line.strip('/n')
        elements = cleaned_line.split(',')
        if elements[0]!='Date':
            date = datetime.strptime (elements[0], '%d-%m-%Y')
            date_list.append(date)
    return date_list

file = open('shampoo_sales.csv','r')
date_list = get_date(file)
for data in date_list:
    print(data.strftime('%d-%m-%Y'))
#print(date_list)
    