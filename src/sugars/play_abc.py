"""
https://pymotw.com/2/abc/

Why use Abstract Base Classes?
Abstract base classes are a form of interface checking more strict than individual hasattr() checks for particular methods. By defining an abstract base class, you can define a common API for a set of subclasses. This capability is especially useful in situations where a third-party is going to provide implementations, such as with plugins to an application, but can also aid you when working on a large team or with a large code-base where keeping all classes in your head at the same time is difficult or not possible.

abc module means Abstract Base Class for python
a special implements that could do check abstract method
"""

import abc

class PluginBase(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def load(self, input):
        """Retrieve data from the input source and return an object."""
        return
    
    @abc.abstractmethod
    def save(self, output, data):
        """Save the data object to the output."""
        return

class RegisteredImplementation(object):
    
    def load(self, input):
        return input.read()
    
    def save(self, output, data):
        return output.write(data)

PluginBase.register(RegisteredImplementation)


#By subclassing directly from the base, we can avoid the need to register the class explicitly.
class SubclassImplementation(PluginBase):
    
    def load(self, input):
        return input.read()
    
    def save(self, output, data):
        return output.write(data)

def test1():
    print 'Subclass:', issubclass(RegisteredImplementation, PluginBase)
    print 'Instance:', isinstance(RegisteredImplementation(), PluginBase)

def test2():
    print 'Subclass:', issubclass(SubclassImplementation, PluginBase)
    print 'Instance:', isinstance(SubclassImplementation(), PluginBase)


"""
Although a concrete class must provide an implementation of an abstract methods, the abstract base class can also provide an implementation that can be invoked via super(). This lets you re-use common logic by placing it in the base class, but force subclasses to provide an overriding method with (potentially) custom logic.
"""
from cStringIO import StringIO

class ABCWithConcreteImplementation(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def retrieve_values(self, input):
        print 'base class reading data'
        return input.read()

class ConcreteOverride(ABCWithConcreteImplementation):
    
    def retrieve_values(self, input):
        base_data = super(ConcreteOverride, self).retrieve_values(input)
        print 'subclass sorting data'
        response = sorted(base_data.splitlines())
        return response

input = StringIO("""line one
line two
line three
""")

reader = ConcreteOverride()
print reader.retrieve_values(input)

class Base(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractproperty
    def value(self):
        return 'Should never get here'


class Implementation(Base):
    
    @property
    def value(self):
        return 'concrete property'


try:
    b = Base()
    print 'Base.value:', b.value
except Exception, err:
    print 'ERROR:', str(err)

i = Implementation()
print 'Implementation.value:', i.value

if __name__ == '__main__':
    test1()
    test2()
    #A side-effect of using direct subclassing is it is possible to find all of the implementations of your plugin by asking the base class for the list of known classes derived from it (this is not an abc feature, all classes can do this).
    for sc in PluginBase.__subclasses__():
        print sc.__name__





