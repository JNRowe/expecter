__all__ = ['expect']


class expect:
    def __init__(self, value):
        self._value = value

    def __eq__(self, other):
        assert self._value == other, ('Expected %s but got %s'
                                      % (repr(self._value), repr(other)))

    def __ne__(self, other):
        assert self._value != other, ('Expected anything except %s but got it'
                                      % repr(self._value))

    def __lt__(self, other):
        assert self._value < other, (
            'Expected something less than %s but got %s'
            % (repr(other), repr(self._value)))

    def __gt__(self, other):
        assert self._value > other, (
            'Expected something greater than %s but got %s'
            % (repr(other), repr(self._value)))

    def __le__(self, other):
        assert self._value <= other, (
            'Expected something less than or equal to %s but got %s'
            % (repr(other), repr(self._value)))

    def __ge__(self, other):
        assert self._value >= other, (
            'Expected something greater than or equal to %s but got %s'
            % (repr(other), repr(self._value)))

    @staticmethod
    def raises(cls):
        return _RaisesExpectation(cls)


class _RaisesExpectation:
    def __init__(self, exception_class):
        self._exception_class = exception_class

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        no_exception_was_raised = not exc_type
        if exc_type is self._exception_class:
            return True
        elif no_exception_was_raised:
            raise AssertionError(
                'Expected an exception of type %s but got none'
                % self._exception_class.__name__)
        else:
            pass
