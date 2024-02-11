class MyClass:
    def __init__(self):
        self._my_property = 0

    @property
    def my_property(self):
        return self._my_property

    @my_property.setter
    def my_property(self, value):
        self._my_property = value
