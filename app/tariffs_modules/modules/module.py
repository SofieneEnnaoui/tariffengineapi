import abc
import time
import statistics
import numpy as np


def current_milli_time(): return int(round(time.time() * 1000))


def timeit(fn):
    t = current_milli_time()
    fn()
    return current_milli_time() - t


class Module(metaclass=abc.ABCMeta):

    #@property
    #@abc.abstractmethod
    def name(self):
        return type(self).__name__

    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def predict(self):
        pass

    def loop(self, number):
        res = []
        for i in range(number):
            res.append(timeit(self.predict))
        return {
            "name": self.name(),
            "iter": number,
            "total": sum(res),
            "min": min(res),
            "quantile25": np.percentile(res, 25),
            "median": statistics.median(res),
            "quantile75": np.percentile(res, 75),
            "max": max(res)
        }
