#!/usr/bin/env python
"""
Distribution script for TAPIS, a program for transcriptome analysis
from isoform sequencing

\author Mike Hamilton
"""
from distutils.core import setup
import sys
SCRIPTS  = ['scripts/run_tapis.py',
            'scripts/polyA.py',
            'scripts/convertSam.py'
            ]

PACKAGES = [ 'tapis'
             ]


REQUIRES = ['SpliceGrapher',
            'numpy',
            'matplotlib',
            'pysam'
            ]

# check for dependencies if we're building or installing
installable = True
if 'build' in sys.argv or 'install' in sys.argv:
    sys.stderr.write('Checking for dependencies...\n')
    for package in REQUIRES:
        try:
            p = __import__( package )
            sys.stderr.write('package "%s" found (version %s)\n' % (package, p.__version__))
        except ImportError:
            installable = False
            sys.stderr.write('\tRequired package `%s` not found\n' % package )
    if not installable:
        sys.exit('Missing dependencies--terminating installation')

setup(name='TAPIS',
      version='0.3.1',
      description='Transcriptome Analysis Pipeline for Isoform Sequencing',
      author='Michael Hamilton',
      author_email='hamiltom@cs.colostate.edu',
      url='combi.cs.colostate.edu/tapis',
      packages=PACKAGES,
      requires=REQUIRES,
      scripts=SCRIPTS,
      license='GNU General Public License'
     )
