from setuptools import setup

setup(
    name='rdopts',
    version='0.1.0',
    py_modules=['rdopts'],
    entry_points= {
        'distutils.commands' : [
            'rdopts = rdopts:Rdopts']}
)
