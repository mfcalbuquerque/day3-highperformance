import numpy as np
import sys
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = int(sys.argv[1])

x = np.linspace(start=float(rank)/size, stop=float(1+rank)/size, num = n//size, endpoint=False)
cosx = np.cos(x)


integral = np.zeros(1)
total = np.zeros(1)


integral[0] = np.sum(cosx)*1.0/n
print("Estimate of integral of cos(x) from %f to %f is %f." % (float(rank)/size, float(1+rank)/size, integral))

comm.Reduce(integral, total, op=MPI.SUM, root=0)


if rank == 0:
    print("With n=%d our estimate of the integral of cos(x) from 0 to 1 is %f." % (n, np.sin(1.0)))
