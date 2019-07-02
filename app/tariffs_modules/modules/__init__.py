from importlib import import_module
from .module import Module
import os


class Factory:

    @classmethod
    def create(cls, name, *args, **kwargs):
        try:
            if '.' in name:
                module_name, class_name = name.rsplit('.', 1)
            else:
                module_name, class_name = name, "".join([x.capitalize() for x in name.split("_")])
            my_module = import_module('.' + module_name, package='tariffs_modules.modules')
            my_class = getattr(my_module, class_name)
            instance = my_class(*args, **kwargs)
        except (AttributeError, ModuleNotFoundError) as e:
            raise ImportError('Error while trying to load module {}.{}: {}'.format(module_name, class_name, str(e)))

        return instance

    @classmethod
    def list_modules(cls):
        exclusion = ['module.py']
        return [x.split('.')[0] for x in os.listdir(os.path.dirname(__file__))
                if not x.startswith('_') and x.endswith('.py') and x not in exclusion]
