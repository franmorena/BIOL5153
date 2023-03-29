#! /usr/bin/env python3

# import modules
import argparse

# create an ArgumentParser Object 
parser = argparse.ArgumentParser(description="this script prints SBASH script with passed parameters/argument and options")

# add positional (required) arguments
parser.add_argument("job", help="title of project/job", type=str)

# add optional arguments
parser.add_argument("-queue", help="which HPC queue is used", default = "comp72", type=str)
parser.add_argument("-walltime", help="maximum walltime designated for a job", default="1", type=int)
parser.add_argument("-nodes", help="number of HPC nodes to utilize for a job", default="1", type=int)
parser.add_argument("-processors", help="number of HPC processors to utilize for a job", default="1", type=int)

# parse arguments
args = parser.parse_args()

# set variables 
job_name = args.job
queue = args.queue 
walltime = args.walltime
num_nodes = args.nodes
num_processors = args.processors

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

print()

print('# job command here')

