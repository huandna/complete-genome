#PBS -N wyx_closgap
#PBS -j oe      
#PBS -l walltime=5000:00:00  
#PBS -l nodes=1:ppn=10
#PBS -q com_q
#PBS -j n
export PATH=/share/apps/anaconda3/bin/python:$PATH

/share/home/chuanlex/yaoxinw/data/methylation/fill_gap_chlamydomonas/our_map/tiqu.py -a newgenome -b material.fasta -c 200result -d final
# a wei  raw_genome
# b materil.fasta
# c result of combine of mumer  & mini 
# d result.fasta
