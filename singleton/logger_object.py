class SingletonObject(object):
    class _SingletonObject():
        def __init__(self):
            self.val = None

        def __str__(self):
            return f"{repr(self)}\n{self.val}" #repr(str) let us avoid infinity recursion in this case

    instance = None

    def __new__(self):
        if not SingletonObject.instance:
            SingletonObject.instance = SingletonObject._SingletonObject()
        return SingletonObject.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, value):
        setattr(self.instance, name, value)
