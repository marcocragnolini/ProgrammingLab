class Model ():
    def fit (self, data):
        raise NotImplementedError('Metodo non implementabile')
    def predict (self, data):
        raise NotImplementedError('Metodo non implementabile')


class Error():
    pass

class NotImplementedError(Error):
    pass
        