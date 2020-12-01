class FunctionsFrameworkException(Exception):
    pass


class InvalidConfigurationException(FunctionsFrameworkException):
    pass


class InvalidTargetTypeException(FunctionsFrameworkException):
    pass


class MissingSourceException(FunctionsFrameworkException):
    pass


class MissingTargetException(FunctionsFrameworkException):
    pass
