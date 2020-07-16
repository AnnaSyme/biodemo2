#!/usr/bin/env python

from distutils.core import setup

LONG_DESCRIPTION = \
'''The program reads one or more input FASTA files.
For each file it computes a variety of statistics, and then
prints a summary of the statistics as output.

The goal is to provide a solid foundation for new bioinformatics command line tools,
and is an ideal starting place for new projects.'''


setup(
    name='biodemo2',
    version='0.1.0.0',
    author='Anna Syme',
    author_email='anna.syme@gmail.com',
    packages=['biodemo2'],
    package_dir={'biodemo2': 'biodemo2'},
    entry_points={
        'console_scripts': ['biodemo2 = biodemo2.biodemo2:main']
    },
    url='https://github.com/GITHUB_USERNAME/biodemo2',
    license='LICENSE',
    description=('A prototypical bioinformatics command line tool'),
    long_description=(LONG_DESCRIPTION),
    install_requires=["biopython"],
)
