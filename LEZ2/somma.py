def sum_list(my_list):
    if not my_list:
        return None
    else:
        sum = 0
        for item in my_list:
            sum = sum + item
        return sum