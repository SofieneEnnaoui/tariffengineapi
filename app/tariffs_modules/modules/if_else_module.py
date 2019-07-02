from .module import Module
from tests.if_else.if_else_fun import Tcom_tot_0_Python_if_else


class IfElseModule(Module):
    """class name must be file name capitalized"""

    #def name(self):
    #    return 'IfElseModule'

    def __init__(self):
        self.__pyInput = (17, 2, 4, 5, 6, 15, 29, 10, 37, 1615, 237, 11, 0, 2697, 7, 27, 1, 5, 4, 4, 1, 1)

    def predict(self):
        Tcom_tot_0_Python_if_else(*self.__pyInput)

