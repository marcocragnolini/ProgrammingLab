class Diff ():
    def __init__ (self, ratio = None):
        if ratio is None:
            self.ratio = 1
        else:
            self.ratio = ratio
    def compute (self,series):
        output = []
        for i in range (len(series)-1):
            diff = series[i+1]-series[i]
            diff = diff/self.ratio
            output.append(diff)
        return output
            
class ExamException (Exception):
    pass