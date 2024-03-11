print('#!/bin/bash')

print('#SBATCH --job-name=example')
print('#SBATCH --partition comp72')
print('#SBATCH --nodes=1')
print('#SBATCH --qos comp')
print('#SBATCH --tasks-per-node=32')
print('#SBATCH --time=72:00:00')
print('#SBATCH -o example_%j.out')
print('#SBATCH -e example_%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=email@uark.edu')

print('module purge')
print('module load intel/18.0.1 impi/18.0.1 mkl/18.0.1')

print('cd $SLURM_SUBMIT_DIR')

print('# job command here')