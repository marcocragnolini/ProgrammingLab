class CSVFile():
    def __init__ (self, name):
        self.name = name
    def get_data (self):
        try:
            my_file = open(self.name, 'r')
            my_list = []
        except Exception:
            return None
        for line in my_file:
            try:
                cleaned_line = line.strip('\n')
                elements = cleaned_line.split(',')
                if elements[0] != 'Date':
                    my_list.append(elements)
            except Exception:
                return None
        return my_list