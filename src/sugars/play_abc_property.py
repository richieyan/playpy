#https://pymotw.com/2/abc/
import abc

class Base(object):
    __metaclass__ = abc.ABCMeta
    
    def value_getter(self):
        return 'Should never see this'
    
    def value_setter(self, newvalue):
        return
    value = abc.abstractproperty(value_getter, value_setter)


class PartialImplementation(Base):
    
    @abc.abstractproperty
    def value(self):
        return 'Read-only'

class Implementation(Base):
    
    _value = 'Default value'
    
    def value_getter(self):
        return self._value

    def value_setter(self, newvalue):
        self._value = newvalue

    value = property(value_getter, value_setter)


try:
    b = Base()
    print 'Base.value:', b.value
except Exception, err:
    print 'ERROR:', str(err)

try:
    p = PartialImplementation()
    print 'PartialImplementation.value:', p.value
except Exception, err:
    print 'ERROR:', str(err)

i = Implementation()
print 'Implementation.value:', i.value

i.value = 'New value'
print 'Changed value:', i.value



class DecoBase(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractproperty
    def value(self):
        return 'Should never see this'
    
    @value.setter
    def value(self, newvalue):
        return


class ImplementationDecoBase(DecoBase):
    
    _value = 'Default value'
    
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, newvalue):
        self._value = newvalue


i = ImplementationDecoBase()
print 'Implementation.value:', i.value

i.value = 'New value'
print 'Changed value:', i.value
