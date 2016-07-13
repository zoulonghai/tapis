========
Tutorial
========
This tutorial is meant as a complete walk-through for identifying
transcripts and poly(A) sites from PacBio reads.

1. Align and clean reads
2. Cluster reads and analyze transcripts and poly(A) sites

Align reads
-----------
**TAPIS** accepts any sorted, indexed BAM file for
long reads but it provides a method that cleans and aligns
reads with high accuracy and efficiency. To align and clean reads
use the following provided script :program:`alignPacBio.py`.  Before
running the script, you will need to run :program:`gmap_build` to
make a genome reference index.  Since version 1.2.1, the alignment script
creates two files, an aligned bamfile and unaligned reads in a FASTA
file (previous versions required merging of individual iterations of alignment/cleaning runs).

.. program-output:: alignPacBio.py --help



Creating indexed, sorted BAM files
----------------------------------

If your cleaned/aligned reads are in the form of a SAM file, you can convert it to a indexed,
sorted BAM file using :program:`convertSam.py`.  

.. program-output:: convertSam.py --help


Running **TAPIS**
-------------------

.. command-output:: run_tapis.py --help 

While **TAPIS** offers many options, default values should work
for most cases.

Interpreting **TAPIS** output
---------------------------
**TAPIS** builds an output directory as follows:

::

   $ tree my_result
     tapis_out
     |-- polyAFigures
     |   |-- gene1.png
     |   |-- gene2.pbg
     |   |-- ...
     |   |-- geneN.png
     |-- novelGraphs
     |   |-- chrom_start_end_strand.pdf
     |   |-- ...
     |-- assembled.gtf
     |-- novelGenes.csv
     |-- novelGenes.fa
     |-- polyA_summary.csv

* **polyAFigures** - contains poly(A) site depictions for genes with
  at least one poly(A) site supported by long reads.
* **novelGraphs** - contains splice graph figures for transcripts not found in within any annotated gene.
* **assembled.gtf** - gene models for transcripts detected in long reads
* **novelGenes.csv** - tab-delimited file containing summary of novel genes detected
    
.. [SG] Rogers, MF, Thomas, J, Reddy, AS, Ben-Hur, A (2012). 
	SpliceGrapher: detecting patterns of alternative splicing 
	from RNA-Seq data in the context of gene models and 
	EST data. *Genome Biol*., 13, 1:R4.
