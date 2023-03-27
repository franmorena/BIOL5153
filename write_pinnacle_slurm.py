#! /usr/bin/env python3

# set variables 
job_name = 'JOB-NAME'
queue = 'comp01' 
walltime = '1'
num_nodes = '32'
num_processors = '24'

#print bash header
print('#! /bin/bash') 

print()

# print SBATH commands 
print('#SBATCH --job-name=' + job_name)
print('#SBATCH --partition', queue)
print('#SBATCH --nodes=1' + str(num_nodes))
print('#SBATCH --qos comp')
print('#SBATCH --tasks-per-node=32')
print('#SBATCH --time=' + str(walltime) + ':00:00')
print('#SBATCH -o test_%j.out')
print('#SBATCH -e test_%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-fmorenad@uark.edu')

print()

# Purge all the modules
print('module purge')

print()

print('cd $SLURM_SUBMIT_DIR')
print('# job command here')
