"""Autogenerated by Nike
Modo 1321
"""

from . import object
from . import result
from . import service
from . import symbol


class Monitor:
    """Monitor objects"""
    def __init__(self, init=None):
        """Initialization of the Monitor class.

        Args:
            init (int):  Total number of steps to initialize with.
        """
        self.init(init)

    def init(self, count):
        """Initialize the monitor with the total number of steps.

        Args:
            count (int): Total number of steps to initialize with.
        """
        pass

    def step(self, value=1):
        """Increment the monitor by one or by step it by an arbitrary amount.

        Args:
            value (int): Amount to step the monitor with.
        """
        pass


class Service:
    """Script query objects."""
    def __init__(self, service):
        """Initialization of the Service class.

        Args:
            service (str): The name of the service to initialize.

        Notes:
            List of possible services: https://modosdk.foundry.com/wiki/Category:ScriptQuery

        Examples:
            # Initialize the command service.
            cmd_srv = lx.Service("commandservice")
            # Select the command 'select.item'.
            cmd_srv.select( "command", "select.item" )
            # Return the commands arguments names.
            print cmd_srv.query("command.argNames")
        """
        pass

    def name(self):
        """Return the name of the script service.

        Returns:
            name (str): The name of the service.
        """
        pass

    def query(self, attribute=None):
        """Query an attribute from the selection.

        Args:
            attribute (str): Name of the attribute to query.

        Returns:
            any: Result of the attribute. Or list of all attributes if set to None
        """
        pass

    def query1(self, attribute=None):
        """Query an attribute from the selection, returning a single value.

        Args:
            attribute (str): Name of the attribute to query.

        Returns:
            any: First returned value.
        """
        pass

    def queryN(self, attribute=None):
        """Query an attribute from the selection, returning a tuple.

        Args:
            attribute (str): Name of the attribute to query.

        Returns:
            tuple: All returned values.
        """
        pass

    def select(self, attribute, element):
        """Select a an attribute (and element) for query.

        Args:
            attribute (str): Service attribute to find
            element (str): Attribute element to select
        """
        pass


def arg():
    """Get the argument string for the script.

    Returns:
        str: Argument passed into a fire and forget script.
    """
    pass


def args():
    """Get the parsed argument tuple for the script.

    Returns:
        tuple[str]: List og args passed into a fire and forget script.
    """
    pass


def bless(cls, name, tags=None, meta=None):
    """Export a class as a server object:

    Notes:
        The class must be derived in part from lxifc base classes, and the first
        class in the hierarchy is the server type. The name must be unique for all
        servers of this same type in the system. Tags are given by a dictionary of
        tag[key] = value pairs. The metaclass is passed as argument to the
        __init__() method, providing global state to customize the class.

    Args:
        cls (object): class to bless
        name (str): the server name
        tags (dict): optional dictionary of server tags
        meta (object): optional metaclass object
    """
    pass


def command(cmd, **kwargs):
    """Execute a command with a variable argument list.

    Args:
        cmd (str): Name of the command to evaluate.
        kwargs (any): Command attributes.
    """
    pass


def eval(cmd):
    """Evaluate a command string.

    Args:
        cmd (str): The command to evaluate.

    Returns:
        any: Single or multiple values.
    """
    pass


def eval1(cmd):
    """Evaluate a command string, returning a single value.

    Args:
        cmd (str): The command to evaluate.

    Returns:
        any: Single value.
    """
    pass


def evalN(cmd):
    """Evaluate a command string, returning a tuple.

    Args:
        cmd (str): The command to evaluate.

    Returns:
        tuple: List of returned values.
    """
    pass


def excResult():
    """Get the exception as an LxResult code."""
    pass


def extract():
    """Extract the Python object referenced from a COM object wrapper."""
    pass


def getQWidget(pyLong):
    """Converts a PyLong object to a PySide QWidget.

    Args:
        pyLong (int|long): Long int that is used to identify a QWidget.

    Returns:
        (QWidget): The representative QWidget from the long.
    """
    pass


def lastResult():
    """Get the result code from the last service or object method called.

    Returns:
        (int): The latest result code.
    """
    pass


def notimpl():
    """Raise 'not implemented' exception.

    Raises:
        NotImplementedError
    """
    pass


def option(option):
    """Get the current state of an option.

    Args:
        option (str): Name of the option to query.

    Returns:
        (str): The current value of the option.
    """
    pass


def out(*args):
    """Output to log.

    Args:
        args (any): arguments to print to the console.
    """
    pass


def outEx():
    """Output the exception state to the log."""
    pass


def queryToggle(cmd):
    """Query a command with a ToggleValue style argument.

    Args:
        cmd (str): THe command to test the current toggled value

    Returns:
        (bool): The state of the toggle.
    """
    pass


def setOption(option, value):
    """Set options that affect how the lx methods act.

    Args:
        option (str): Option to set value on.
        value (any): Value to set option to.
    """
    pass


def test(cmd):
    """Test the state of a toggle argument.

    Args:
        cmd (str): The command to test the current toggled value

    Returns:
        (bool): The state of the toggle.
    """
    pass


def testifc(cls, guid, meta=None):
    """Test an interface GUID against a class:

    Args:
        cls (object): The class to test.
        guid (str): Globally Unique Identifier
        meta (object):

    Returns:
        bool: True if guid matches class.
    """
    pass


def throw(code, quiet=False):
    """Raise a result code exception.

    Args:
        code (int): lx.result code values.
        quiet (bool): True, if you want to error to not show in the console.
    """
    pass


def trace(enable):
    """Toggle extra Event Log output for each lx function call.

    Args:
        enable (bool): If True, enables the lx trace.
    """
    pass