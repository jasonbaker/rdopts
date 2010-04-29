"""distutils.command.x

Implements the Distutils 'x' command.
"""

# created 2000/mm/dd, John Doe

__revision__ = "$Id$"

import sys
from distutils.core import Command


class Rdopts(Command):

    # Brief (40-50 characters) description of the command
    description = "Read options from setup.cfg"

    # List of option tuples: long name, short name (None if no short
    # name), and help string.
    user_options = [('command', 'c',
                     "The command to read options for"),
                    ('option', 'o',
                     "The name of the option to read"),
                   ]


    def initialize_options (self):
        self.command = None
        self.option = None

    def finalize_options (self):
        if self.command is None or self.option is None:
            sys.stderr.flush()
            sys.stdout.flush()
            print >> sys.stderr, 'Must specify both command AND option'
            sys.exit(1)

    def run (self):
        pass

