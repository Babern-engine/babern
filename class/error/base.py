import sys
class MissingModule:
    _NOT_IMPLEMENTED_ = True

    def __init__(self, name, urgent=0):
        self.name = name
        exc_type, exc_msg = sys.exc_info()[:2]
        self.info = str(exc_msg)
        self.reason = "%s: %s" % (exc_type.__name__, self.info)
        self.urgent = urgent
        if urgent:
            self.warn()

    def __getattr__(self, var):
        if not self.urgent:
            self.warn()
            self.urgent = 1
        missing_msg = "%s module not available (%s)" % (self.name, self.reason)
        raise NotImplementedError(missing_msg)

    def __nonzero__(self):
        return False

    __bool__ = __nonzero__

    def warn(self):
        msg_type = 'import' if self.urgent else 'use'
        message = '%s %s: %s\n(%s)' % (msg_type, self.name, self.info, self.reason)
        try:
            import warnings
            level = 4 if self.urgent else 3
            warnings.warn(message, RuntimeWarning, level)
        except ImportError:
            print(message)


class error(RuntimeError):
    RuntimeError

def get_error() -> str: ...