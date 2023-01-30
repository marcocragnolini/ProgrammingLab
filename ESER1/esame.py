class MovingAverage():
    def __init__(self,window):
            self.window = window
    def compute (self,series):
        avg_list = []
        for i in range (len(series)-self.window+1):
            sum = 0
            for i in range (i,i+self.window):
                sum += series[i]
            avg = sum/self.window
            avg_list.append(avg)
        return avg_list

class ExamException (Exception):
    pass

