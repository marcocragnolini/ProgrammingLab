def sum_list (my_list, sum):
    if my_list == None:
        return None
    for item in my_list:
        sum += item
    return sum

my_list = [1,2,3,4,5,6,7,8,9]
ris = sum_list (my_list, 0)
print (ris)