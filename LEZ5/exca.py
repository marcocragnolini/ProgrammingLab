class CSVFile():
    def __init__ (self, name):
        self.can_open = True
        self.name = name
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_open = False
            print ("Errore:{}".format(e))
    def get_data (self):
        if self.can_open:
            my_file = open(self.name)
            my_list = []
            for line in my_file:
                cleaned_line = line.strip('\n')
                elements = cleaned_line.split(',')
                if elements[0] != 'Date':
                    my_list.append(elements)
            return my_list
        else:
            return None
        
    
