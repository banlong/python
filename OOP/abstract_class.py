import abc
class Shape(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def method_to_implement(self, input):
        """Method documentation"""
        return

class Rectangle(Shape):
    def __init__(self, name):
        self.shape = name

class PluginBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def load(self, input):
        """Retrieve data from the input source
        and return an object.
        """
    @abc.abstractmethod
    def save(self, output, data):
        """Save the data object to the output."""

class SubclassImplementation(PluginBase):

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)


if __name__ == '__main__':
    print('Subclass:', issubclass(SubclassImplementation,PluginBase))
    print('Instance:', isinstance(SubclassImplementation(), PluginBase))


rect = Rectangle("Hello")
print(rect.shape)