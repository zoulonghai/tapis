from SpliceGrapher.formats import fasta
itr = fasta.fasta_itr('all.fa')
counts = 0
for rec in itr:
    counts += len(rec.sequence)
    
