# Pypar #
Pypar is an efficient but easy-to-use module that allows programs written in Python to run in parallel on multiple processors and communicate using message passing. Pypar provides bindings to a subset of the message passing interface standard MPI.

# Breaking News #
We are moving Pypar to Github to facilitate more collaboration. This page and the Google repository will remain as is for the foreseeable future, but if you want the latest features please get Pypar from https://github.com/daleroberts/pypar

# Features #
  * **Flexibility:** Pypar allows communication of general Python objects of any type.
  * **Intuitive API:** The user need only specify what to send and to which processor. Pypar takes care of details about data types and MPI specifics such as tags, buffers, communication status and communicators. Receiving is analogous.
  * **Efficiency:** Full bandwidth of C-MPI programs is achieved for consecutive Numerical arrays. Latency is less than twice that of pure C-MPI programs. Test programs to verify this are included (pytiming.py, ctiming.c)
  * **Lightweight:** Pypar consists of just two files: mpiext.c and pypar.py
  * **Python interpreter is not modified:** Parallel python programs need only import the pypar module.

# Dependencies and Installation #
  * Pypar requires Python, numpy, C compiler and MPI C library such as openmpi
  * Pypar installs with distutils: python setup.py install
  * Pypar is mostly used on Linux systems, but has been tested on others too.

# Example #
```
import pypar                                       # Import module and initialise MPI 

proc = pypar.size()                                # Number of processes as specified by mpirun
myid = pypar.rank()                                # Id of of this process (myid in [0, proc-1]) 
node = pypar.get_processor_name()                  # Host name on which current process is running

print 'I am proc %d of %d on node %s' % (myid, proc, node)

if myid == 0:                                      # Actions for process 0:
  msg = 'P0'  
  pypar.send(msg, destination=1)                   # Send message to proces 1 (right hand neighbour)
  msg = pypar.receive(source=proc-1)               # Receive message from last process
      
  print 'Processor 0 received message "%s" from processor %d' % (msg, proc-1)

else:                                              # Actions for all other processes:

  source = myid-1                                  # Source is the process to the left
  destination = (myid+1)%proc                      # Destination is process to the right
                                                   # wrapped so that last processor will 
						   # send back to proces 0  
  
  msg = pypar.receive(source)                      # Receive message from source 
  msg = msg + 'P' + str(myid)                      # Update message     
  pypar.send(msg, destination)                     # Send message to destination   

pypar.finalize()                                   # Stop MPI 
```

# Some projects and publications that use Pypar #

  * [Managing a pool of MPI processes with Python and Pypar](http://www.shocksolution.com/2010/04/17/managing-a-pool-of-mpi-processes-with-python-and-pypar)
  * [Simplifying the parallelization of scientific codes by a function-centric approach in Python](http://iopscience.iop.org/1749-4699/3/1/015003/fulltext)
  * [Parallelizing PDE Solvers Using the Python Programming Language (PDF)](http://www.google.com.au/url?sa=t&source=web&cd=3&sqi=2&ved=0CCIQFjAC&url=http%3A%2F%2Fheim.ifi.uio.no%2F~xingca%2FDR%2FCai_Ref18.pdf&rct=j&q=PDE%20Solvers%20pypar&ei=g1LyTOSBIYP2vwPX8bTXDQ&usg=AFQjCNFeVRgL9GkeYTyNv2J9jpHchLmFQA&sig2=fwPP9sBR8ANiQcq1yhIyTw&cad=rja)
  * [Python for CFD (PDF)](http://www.google.com.au/url?sa=t&source=web&cd=17&ved=0CD4QFjAGOAo&url=http%3A%2F%2Fwww.aero.iitb.ac.in%2F~prabhu%2Fresearch%2Fpapers%2Fpr_scipy04.pdf&rct=j&q=Prabhu%20Ramachandran%20pypar&ei=6lTyTJ7nEoj2vwO7xemWDg&usg=AFQjCNEwqG62zc6GFV1Kq2Oz1Y65DZ4B4Q&sig2=oFA6SeUwca_I_DNyw3w68g&cad=rja)
  * [ANUGA Hydrodynamic Modelling](https://datamining.anu.edu.au/anuga)
  * [EQRM Earthquake Risk Modelling](http://sourceforge.net/projects/eqrm)
  * [Volcanic Ash Modelling](http://www.aifdr.org/projects/aim)