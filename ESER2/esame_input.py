class Diff ():
    def __init__ (self, ratio = 1):
            try:
                self.ratio = float(ratio)
            except ValueError as v:
                raise ExamException ('Errore: {}'.format(v))
            except TypeError as t:
                raise ExamException ('Errore: {}'.format(t))
            except Exception as e:
                raise ExamException ('Errore: {}'.format(e))
            if self.ratio <= 0:
                raise ExamException ('Errore: il ratio è debolmente negativo')
    def compute (self,series):
        if series is None:
            raise ExamException ('Errore: la lista è None')
        if not isinstance(series,list):
            raise ExamException ('Errore: non mi è stata data una lista')
        if len(series)<=1:
            raise ExamException ('Errore: la lista è vuota o ha solo un elemento')
        num_series = []
        for item in series:
            try:
                float_item = float(item)
                num_series.append(float_item)
            except ValueError as v:
                raise ExamException ('Errore: {}'.format(v))
            except TypeError as t:
                raise ExamException ('Errore: {}'.format(t))
            except Exception as e:
                raise ExamException ('Errore: {}'.format(e))
        output = []
        for i in range (len(num_series)-1):
            diff = num_series[i+1]-num_series[i]
            diff = diff/self.ratio
            output.append(diff)
        return output
            
class ExamException (Exception):
    pass



