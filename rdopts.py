# Copyright 2010 Jason Baker. All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without modification, are
# permitted provided that the following conditions are met:
# 
#     1. Redistributions of source code must retain the above copyright notice, this list of
#       conditions and the following disclaimer.
# 
#    2. Redistributions in binary form must reproduce the above copyright notice, this list
#       of conditions and the following disclaimer in the documentation and/or other materials
#       provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY Jason Baker ``AS IS'' AND ANY EXPRESS OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL Jason Baker OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# The views and conclusions contained in the software and documentation are those of the
# authors and should not be interpreted as representing official policies, either expressed
# or implied, of Jason Baker.


"""
rdopts - read options from setup.cfg
"""
import sys, os
from distutils.core import Command
from distutils.log import set_threshold, ERROR
set_threshold(ERROR)
from ConfigParser import SafeConfigParser

class Rdopts(Command):

    # Brief (40-50 characters) description of the command
    description = "Read options from setup.cfg"

    # List of option tuples: long name, short name (None if no short
    # name), and help string.
    user_options = [('command=', 'c',
                     "The command to read options for"),
                    ('option=', 'o',
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
        config = SafeConfigParser()
        config.read(['./setup.cfg'])
        if not config.has_section(self.command) or config.has_option(self.command, self.option):
            print ''
            return

        val = config.get(self.command, self.option)
        print val
