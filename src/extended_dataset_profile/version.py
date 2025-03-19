from packaging.version import Version

try:
    from ._version import __version__
except ImportError:
    __version__ = "0.0.0+dirty"


CURRENT_VERSION = Version(__version__)
