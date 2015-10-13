"""
3. Object Oriented Concepts

1. Write a class called Mammal.
    * Mammal should have a method called 'speak' that returns 'hello'.
    * Mammal should have a method called 'legs' that returns 2.
    * Allow the output of 'legs' to be overwritten by modifying the _legs attribute of the Mammal
      class.

2. Write a class called Cat that inherits from Mammal.
    * Cat's speak method should return 'meow'. Don't define a speak method. Inherit it.
    * Cat's 'legs' method should return 2. Dont' define a 'legs' method. Inherit it.

3. Write a class called Dog that inherits from Mammal.
    * Dog's speak method should return 'arf'
    * Define a method on Dog that overrides Mammal's legs method. It should return the output of
      Mammal's legs method multiplied by 2.

4. Write a test that illustrates an attribute defined in the `__init__` method of 'Mammal' is not
   accessible to Dog or Cat when preceded by a double-underscore, but an attribute preceded by a
   single-underscore or no underscore is.

5. Write a new Dog class called Dog2 that doesn't inherit from Mammal. It should behave the same way.

"""


class Mammal(object):
    """Base class Mammal
    """
    _legs = 2
    _speak = 'hello'

    def __init__(self):
        # different types of attribute to illustrate accessibility
        self.body = 'fur'
        self._temperature = 'warm-blooded'
        self.__type = 'mammal'

    def speak(self):
        # method that returns 'hello'.
        return self._speak

    def legs(self):
        # method that returns the value of _legs.
        return self._legs

    # methods to illustrate accessibility of attributes:
    def info_type(self):
        return 'Type: ' + self.__type

    def info_temp(self):
        return 'Temperature: ' + self._temperature

    def info_body(self):
        return 'Body: ' + self.body


class Cat(Mammal):
    """Base clas Cat that inherits from Mammal
    """
    _speak = 'meow'

    def __init__(self):
        # different types of attribute to illustrate accessibility
        super(Cat, self).__init__()
        self.body = 'cat-fur'
        self._temperature = 'cat-warm-blooded'
        self.__type = 'cat-mammal'


class Dog(Mammal):
    """Base class Dog that inherits from Mammal and overrides Mammal's legs method.
    """
    _speak = 'arf'

    def __init__(self):
        # different types of attribute to illustrate accessibility
        super(Dog, self).__init__()
        self.body = 'dog-fur'
        self._temperature = 'dog-warm-blooded'
        self.__type = 'dog-mammal'

    def legs(self):
        return super(Dog, self).legs() * 2


class Dog2(Dog):
    """Base class Dog2 that inherit from Dog.

    Note: Another way to accomplish the task is rewriting Dog2 class with Mammal's and Dog's
    class information, but we lose the ability of legs method to return the output of
    Mammal's legs method multiplied by 2, it should be explicit now (Dog3 class).
    """
    def __init__(self):
        super(Dog2, self).__init__()


class Dog3():
    """Base class Dog3, with no inheritance, and legs method does not depends on Mammal.
    """
    _speak = 'arf'
    _legs = 4

    def speak(self):
        # method that returns 'arf'.
        return self._speak

    def legs(self):
        # method that returns the value of _legs.
        return self._legs
