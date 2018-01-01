"""
https://pymotw.com/2/abc/

Why use Abstract Base Classes?
Abstract base classes are a form of interface checking more strict than individual hasattr() checks for particular methods. By defining an abstract base class, you can define a common API for a set of subclasses. This capability is especially useful in situations where a third-party is going to provide implementations, such as with plugins to an application, but can also aid you when working on a large team or with a large code-base where keeping all classes in your head at the same time is difficult or not possible.

abc module means Abstract Base Class for python
a special implements that could do check abstract method
"""

from abc import ABCMeta, abstractmethod
class AbstractClassExample(ABC):
 
    def __init__(self, value):
        self.value = value
        super().__init__()
    
    @abstractmethod
    def do_something(self):
        pass
