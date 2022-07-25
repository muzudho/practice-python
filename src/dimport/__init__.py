"""
📖 [How to Dynamically Load Modules or Classes in Python](https://www.geeksforgeeks.org/how-to-dynamically-load-modules-or-classes-in-python/)  
📖 [How to dynamically load a Python class](https://stackoverflow.com/questions/547829/how-to-dynamically-load-a-python-class)  
"""


class Dimport:
    @staticmethod
    def load(module_name, class_name):
        # __import__ method used
        # to fetch module
        module = Dimport.load_module(module_name)

        # getting attribute by
        # getattr() method
        return getattr(module, class_name)

    @staticmethod
    def load_module(name):
        components = name.split('.')
        mod = __import__(components[0])
        for comp in components[1:]:
            mod = getattr(mod, comp)

        return mod
