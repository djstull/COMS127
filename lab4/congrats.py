import inspect
def congrats(name):
    return inspect.getargspec(name).args

