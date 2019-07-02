import abc
import redis
import pickle
import datetime


class MemoryInterface(metaclass=abc.ABCMeta):
    """
    Memory Interface to support multiple data sources
    Data structure has to be an equivalent of a dict {str -> str}
    """

    @abc.abstractmethod
    def set(self, key, value):
        """ Set the value corresponding to key, override value if key already exists """
        pass

    @abc.abstractmethod
    def get(self, key):
        """
        Search and return the value corresponding of a key

        :param key: key to search
        :return: value if key exists, None otherwise
        """
        pass

    @abc.abstractmethod
    def keys(self):
        """
        List all keys available in memory
        :return: key list
        """
        pass

    @abc.abstractmethod
    def pop(self, key):
        """
        Delete and return value of a key
        :return: value
        """
        pass


class InMemory(MemoryInterface):

    def __init__(self):
        self._data = {}

    def set(self, key, value):
        self._data[str(key)] = value

    def get(self, key):
        return self._data.get(str(key), None)

    def keys(self):
        return list(self._data.keys())

    def pop(self, key):
        return self._data.pop(str(key))


class Redis(MemoryInterface):

    def __init__(self, configuration):
        self._r = redis.Redis(**configuration)

    def set(self, key, value):
        self._r.setex(str(key), datetime.timedelta(days=1), pickle.dumps(value))

    def get(self, key):
        return pickle.loads(self._r.get(str(key)))

    def keys(self):
        return self._r.keys()

    def pop(self, key):
        d = self.get(str(key))
        self._r.delete(str(key))
        return d
