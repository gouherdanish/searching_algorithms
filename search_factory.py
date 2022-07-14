from abc import ABC, abstractmethod
import utils

class SearchFactory:
    registry={}
    @classmethod
    def register(cls,name):
        def inner_wrapper(wrapped_class):
            cls.registry[name] = wrapped_class
            return wrapped_class
        return inner_wrapper
    
    @classmethod
    def get_handler(cls,name):
        return cls.registry[name]

class Search(ABC):
    @abstractmethod
    def search(arr,target):
        pass

@SearchFactory.register('linear')
class BinarySearch(Search):
    def search(arr,target):
        return utils.binary_search(arr,target)

@SearchFactory.register('binary')
class LinearSearch(Search):
    def search(arr,target):
        return utils.linear_search(arr,target)