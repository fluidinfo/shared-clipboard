#!/usr/bin/env python

import os


# Utility function to read the README file.
# Credit: http://pypi.python.org/pypi/an_example_pypi_project
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

d = dict(name='shared_clipboard',
         version='0.0.1',
         provides=['shared_clipboard'],
         maintainer='Fluidinfo Inc.',
         maintainer_email='info@fluidinfo.com',
         url='https://github.com/fluidinfo/shared-clipboard',
         download_url='https://github.com/fluidinfo/shared-clipboard',
         packages=['shared_clipboard'],
         keywords=['twisted function retry'],
         classifiers=[
             'Programming Language :: Python',
             'Development Status :: 4 - Beta',
             'Intended Audience :: Developers',
             'License :: OSI Approved :: Apache Software License',
             'Operating System :: OS Independent',
             'Topic :: Software Development :: Libraries :: Python Modules',
             ],
         description=('Classes for saving, retrieving and clearing '
                      'shared clipboards stored in Fluidinfo.'),
         )

try:
    from setuptools import setup
    _ = setup  # Keeps pyflakes from complaining.
except ImportError:
    from distutils.core import setup
else:
    d['install_requires'] = ['fom']

setup(**d)
