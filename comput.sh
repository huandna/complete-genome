#PBS -N wyx_gap
#PBS -l nodes=1:ppn=20
#PBS -j oe
#PBS -l walltime=5000:00:00
#PBS -q com_q
export PATH=/share/apps/anaconda3/bin/python:$PATH
outdir=/share/home/chuanlex/yaoxinw/data/methylation/fill_gap_chlamydomonas/new_read_out
cd $outdir
align=/share/home/chuanlex/yaoxinw/data/methylation/fill_gap_chlamydomonas/nanopore_newgenme_aln
gapfile=/share/home/chuanlex/yaoxinw/data/methylation/fill_gap_chlamydomonas/newpos
rate=1.0
yul=200
/share/home/chuanlex/yaoxinw/data/methylation/fill_gap_chlamydomonas/mini_gap_fill.py -a ${gapfile} -b ${align} -c ${rate} -d ${outdir}/zongji200 -e ${yul} 
