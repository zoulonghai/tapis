=========
Get TAPIS
=========

Required packages
=================
The following packages are required for TAPIS core functions.
Version numbers correspond to those tested during development.

- SpliceGrapher_ (v0.2.4 )
- Pysam_ (v0.8.1)
- matplotlib_ (v1.3.1)
- bx-python_ (v0.5.0)
- NumPy_ (v1.8.2)
- GMAP_ (2016-04-01) note: version 2015-07-23 is incompatible

Download
========
current release: v1.2.1

TAPIS is hosted on bitbucket https://bitbucket.org/comp_bio/tapis

Install 
=======
.. code-block:: none

		$ tar zxvf tapis_<version>.tgz
		$ cd tapis_<version>.tgz
		$ python setup.py install

.. note::

   To install in a user directory, use the option:

   .. code-block:: none

		   --home=/Path/To/Local/Library

      

.. _SpliceGrapher: http://splicegrapher.sourceforge.net/
.. _Pysam: https://code.google.com/p/pysam/
.. _matplotlib: http://matplotlib.org/
.. _bx-python: https://pypi.python.org/pypi/bx-python/0.7.3
.. _NumPy: http://www.numpy.org/
.. _GMAP: http://research-pub.gene.com/gmap/
