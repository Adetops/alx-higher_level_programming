class LockedClass:
    def __setattr__(self, name, value):
        if not hasattr(self, name) and name != 'first_name':
            raise AttributeError("'{}' object has ".format("LockedClass") +
                "no attribute '{}'".format(name))
        super().__setattr__(name, value)
