from setuptools import setup

README_TEXT = open('./README.rst').read()

setup(
    name='rdopts',
    version='0.1.2',
    py_modules=['rdopts'],
    long_description=README_TEXT,
    description='A custom setuptools command for reading from setup.cfg',
    entry_points= {
        'distutils.commands' : [
            'rdopts = rdopts:Rdopts']}
)
