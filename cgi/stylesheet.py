"""
A module with a simple data class that stores the arguments passed to it in self to implement styles
"""


class Style:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
