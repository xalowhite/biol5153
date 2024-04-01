

print('#!/bin/bash')

job_name = 'dna'
partition = 'comp72'
nodes = '1'
qos ='comp'
tasks_per_node ='32'
time = '72:00:00'
email = 'cmw070@uark.edu'

print('#SBATCH --job-name=' + str(job_name))
print('#SBATCH --partition' + str(partition))
print('#SBATCH --nodes=' + (nodes))
print('#SBATCH --qos ' + (qos))
print('#SBATCH --tasks-per-node=' + (tasks_per_node))
print('#SBATCH --time=' + (time))
print('#SBATCH -o example_%j.out')
print('#SBATCH -e example_%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=(email)')

print('module purge')
print('module load intel/18.0.1 impi/18.0.1 mkl/18.0.1')

print('cd $SLURM_SUBMIT_DIR')

print('# job command here')