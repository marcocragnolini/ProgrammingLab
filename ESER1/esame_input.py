class MovingAverage():
    def __init__(self,window):
        if isinstance (window,float):
            raise ExamException ('Errore: la finestra è un decimale')
        try:
            self.window = int(window)
        except ValueError as v:
            raise ExamException ('Errore: {}'.format(v))
        except TypeError as t:
            raise ExamException ('Errore: {}'.format(t))
        except Exception as e:
            raise ExamException ('Errore: {}'.format(e))
        if self.window <= 0:
            raise ExamException ('Errore: la finestra è debolmente negativa')
    def compute (self,series):
        numerical_series = []
        if series is None:
            raise ExamException ('Errore: la serie è None')
        if not isinstance(series,list):
            raise ExamException ('Errore: la serie non è una lista')
        for item in series:
            try:
                item_to_append = float(item)
                numerical_series.append(item_to_append)
            except ValueError as v:
                raise ExamException ('Errore: {}'.format(v))
            except TypeError as t:
                raise ExamException ('Errore: {}'.format(t))
            except Exception as e:
                raise ExamException ('Errore: {}'.format(e))
        if self.window <= 0:
            raise ExamException ('Errore: la finestra è debolmente negativa')
        if self.window > len(numerical_series):
            raise ExamException ('Errore: la finestra è più lunga della serie')
        if numerical_series is None:
            raise ExamException ('Errore: la serie è None')
        if len(numerical_series)==0:
            raise ExamException ('Errore: la serie è vuota')
        avg_list = []
        for i in range (len(numerical_series)-self.window+1):
            sum = 0
            for i in range (i,i+self.window):
                sum += numerical_series[i]
            avg = sum/self.window
            avg_list.append(avg)
        return avg_list

class ExamException(Exception):
    pass

#moving_average = MovingAverage (2)
#results = moving_average.compute([1.33,2.67,23,7])
#print(results)





