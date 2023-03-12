from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

summ = np.empty(size, dtype=np.int8)
summ[:] = rank


if rank == 0:
    print("This is the summation over the rank 0: ",summ.sum())
else:
    print("And the summation over the rank {} is {}.".format(rank, summ.sum()))
