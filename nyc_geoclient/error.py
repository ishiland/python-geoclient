class GeoclientError(Exception):
    def __init__(self, message, result=None):
        super(GeoclientError, self).__init__(message)
        self.result = result
