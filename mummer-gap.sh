#PBS -N wyx_nucmer
#PBS -j oe      
#PBS -l walltime=5000:00:00  
#PBS -l nodes=1:ppn=10
#PBS -q com_q
#PBS -j n
export PATH=/share/home/chuanlex/xieshangqian/software/MUM4.0/bin:$PATH
cd /share/home/chuanlex/yaoxinw/data/methylation/fill_gap_chlamydomonas/our_map 
nucmer --mum -l 100 -c 1000 -d 10 --banded -D 5 /share/home/chuanlex/yaoxinw/data/methylation/chlamydomonas_reinhardtii_v5.5/GCA_000002595.3_Chlamydomonas_reinhardtii_v5.5_genomic.fna /share/home/chuanlex/yaoxinw/data/methylation/fill_gap_chlamydomonas/our_map/bridged_p_ctg.fa
delta-filter -i 95 -o 95 out.delta > out.best.delta
dnadiff -d out.best.delta
#mummerplot out.best.delta --fat -f --png



