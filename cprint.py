"""Module for quick printing in colour, on Unix only."""

END = '\033[0m'
BLACK = '\033[30m'
BRIGHT_BLACK = '\033[90m'
RED = '\033[31m'
BRIGHT_RED = '\033[91m'
GREEN = '\033[32m'
BRIGHT_GREEN = '\033[92m'
YELLOW = '\033[33m'
BRIGHT_YELLOW = '\033[93m'
BLUE = '\033[34m'
BRIGHT_BLUE = '\033[94m'
MAGENTA = '\033[35m'
BRIGHT_MAGENTA = '\033[95m'
CYAN = '\033[36m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[37m'
BRIGHT_WHITE = '\033[97m'
TEMPLATE = "%%s%%s%s" % END

def black(text):
    """Print in black."""
    print TEMPLATE % (BLACK, text)

def bblack(text):
    """Print in bright black (gray)."""
    print TEMPLATE % (BRIGHT_BLACK, text)

def red(text):
    """Print in red."""
    print TEMPLATE % (RED, text)

def bred(text):
    """Print in bright red."""
    print TEMPLATE % (BRIGHT_RED, text)

def green(text):
    """Print in green."""
    print TEMPLATE % (GREEN, text)

def bgreen(text):
    """Print in bright green."""
    print TEMPLATE % (BRIGHT_GREEN, text)

def blue(text):
    """Print in blue."""
    print TEMPLATE % (BLUE, text)

def bblue(text):
    """Print in bright blue."""
    print TEMPLATE % (BRIGHT_BLUE, text)

def cyan(text):
    """Print in cyan."""
    print TEMPLATE % (CYAN, text)

def bcyan(text):
    """Print in bright cyan."""
    print TEMPLATE % (BRIGHT_CYAN, text)

def yellow(text):
    """Print in blue."""
    print TEMPLATE % (YELLOW, text)

def byellow(text):
    """Print in bright yellow."""
    print TEMPLATE % (BRIGHT_YELLOW, text)

def magenta(text):
    """Print in magenta."""
    print TEMPLATE % (MAGENTA, text)

def bmagenta(text):
    """Print in bright magenta."""
    print TEMPLATE % (BRIGHT_MAGENTA, text)

def white(text):
    """Print in white (light gray)."""
    print TEMPLATE % (WHITE, text)

def bwhite(text):
    """Print in bright white (max white)."""
    print TEMPLATE % (BRIGHT_WHITE, text)
