def sum_list (my_list):
    sum = 0
    for item in my_list:
        sum = sum + item
    return sum

my_list = [1,2,3,4,5]
ris = sum_list (my_list)
print (ris)