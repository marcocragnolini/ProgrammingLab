

def sum_csv (file_name):
    can_open = True
    try:
        my_file = open(file_name, 'r')
        if not my_file:
            return None
        if my_file is None:
            return None
        my_file.readline()
    except OSError:
        can_open = False
    if can_open:
        values = []
        my_file = open(file_name, 'r')
        for line in my_file:
            elements = line.split(',')
            if elements[0] != 'Date':
                try:
                    value = float(elements[1])
                    values.append(value)
                except Exception:
                    pass
        sum = 0
        for item in values:
            sum += item
        return sum
    else:
        return None

