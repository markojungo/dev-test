"""
A dictionary whose values are only evaluated on access.
"""
from functools import partial


class LazyDict(dict):
    """
    A lazy dictionary implementation which will try
    to evaluate all values on access and cache the
    result for later access.
    """

    def set_lazy(self, key, item, *args, **kwargs):
        """
        Allow the setting of a callable and arguments
        as value of dictionary.
        """
        if callable(item):
            item = partial(item, *args, **kwargs)
        super(LazyDict, self).__setitem__(key, item)

    def __getitem__(self, key):
        item = super(LazyDict, self).__getitem__(key)
        try:
            self[key] = item = item()
        except TypeError:
            pass
        return item
