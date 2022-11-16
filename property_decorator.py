# Use @property decorator on any method in the class to use the method as a property.
# Use the following three decorators to define a property:
# @property : Declares the method as a property.
# @<property-name>.setter: Specifies the setter method for a property that sets the value to a property.
# @< property-name>.deleter: Specifies the delete method as a property that deletes a property.

class student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    # The deleter would be invoked when you delete the property using keyword del.
    # Once you delete a property, you cannot access it again using the same instance.
    @name.deleter
    def name(self):
        del self.__name
