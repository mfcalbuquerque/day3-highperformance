from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
#size = comm.Get_size()
#rank = comm.Get_rank()

def matvec(comm, A, x):
    m = A.shape[0]
    p = comm.Get_size()
    xg = np.zeros(m*p,dtype='i')
    comm.Allgather([x, MPI.INT], [xg, MPI.INT])
    y = np.dot(A,xg)
    
    return y

kkk=matvec(comm, np.array([[1,2,3],[4,5,6],[7,8,9]]), np.array([1,2,3]))
print(kkk)
