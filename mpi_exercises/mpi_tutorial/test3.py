from mpi4py import MPI
import numpy as np

amode = MPI.MODE_WRONLY|MPI.MODE_CREATE
comm = MPI.COMM_WORLD
fh = MPI.File.Open(comm, "./datafile.contig", amode)

buff_data = np.empty(10, dtype=np.int8)
buff_data[:] = comm.Get_rank()

offset = comm.Get_rank()*buff_data.nbytes
fh.Write_at_all(offset, buff_data)

print(fh)
fh.Close()
