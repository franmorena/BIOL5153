---
title: "assgn3"
author: "Fran Morena"
date: "2023-03-09"
output: html_document
editor_options: 
  markdown: 
    wrap: 72
---

**1.**\
\$ pin\
\$ rsync -av \~/Desktop/watermelon_files/mt_genomes
[fmorenad\@hpc-portal2.hpc.uark.edu](mailto:fmorenad@hpc-portal2.hpc.uark.edu){.email}:mt_genomes/\
**2.**\
\$ scp \~/Desktop/BIOL5153/unknown.fa
[fmorenad\@hpc-portal2.hpc.uark.edu](mailto:fmorenad@hpc-portal2.hpc.uark.edu){.email}:mt_genomes/\
**3.**\
\$ nano assn3.slurm

copy of my slurm below.

#!/bin/bash

#SBATCH --job-name=assn3 #SBATCH --partition comp01 #SBATCH --nodes=1\
#SBATCH --qos comp #SBATCH --tasks-per-node=1 #SBATCH --time=00:10:00\
#SBATCH -o %j.out #SBATCH -e %j.err #SBATCH --mail-type=ALL #SBATCH
--[mail-user=fmorenad\@uark.edu](mailto:mail-user=fmorenad@uark.edu){.email}\
\
module purge module load blast/2.9.0+\
\
cd \$SLURM_SUBMIT_DIR\
\
cat \*.fasta \> genomes.fas makeblastdb -in genomes.fas -dbtype nucl\
blastn -query unknown.fa -db genomes.fas \> unknown.vs.genomes.blastn\

**4.**\
rsync -av
[fmorenad\@hpc-portal2.hpc.uark.edu](mailto:fmorenad@hpc-portal2.hpc.uark.edu){.email}:mt_genomes/
\~/Desktop/watermelon_files/mt_genomes

**5.** \* 0.120714secs \* Cucurbita

**6.** \$ cd \~/Desktop/BIOL5153/assn/BIOL5153/\
\$ git remote add origin <https://github.com/franmorena/BIOL5153> \$ git
add assn-03.md\
\$ git commit\
\$ git push -u origin main \$
