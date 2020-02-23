class AccessViolationError(Exception):
    def __init__(self, message:str):
        self.__str__ = message

class ExactProcessError(Exception):
    def __init__(self, message:str):
        self.__str__ = message