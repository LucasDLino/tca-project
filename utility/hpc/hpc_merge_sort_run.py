from mpi4py import MPI
import subprocess

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0:
        subprocess.run(["mpiexec", "-n", "4", "python", "utility/hpc/hpc_merge_sort.py"])

if __name__ == "__main__":
    main()