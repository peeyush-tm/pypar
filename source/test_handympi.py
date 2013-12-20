from handympi import foreach, MY_RANK, NUM_NODES
from pylab import *
import sys
import time

N=10000000   # numbers
M=30         # sets

if len(sys.argv)>1:
    N = int(sys.argv[1])

def f(N):
    y = arccos(1.0-2*rand(N))
    return 2.0*y.sum()/N

Ns = [N]*30

if MY_RANK==0:
    print "Beginning run with", NUM_NODES, "nodes"
    t1=time.time()

result = foreach(f, Ns, finalRun=False)

if MY_RANK==0:
    print result
    print "in between runs..."

result = foreach(f, Ns)

if MY_RANK==0:
    print result
    t2=time.time()
    delta=t2-t1
    nums = N*M*2
    print "that's it!", delta, "seconds for ", nums, "numbers"
    print "So ", delta/nums, "seconds per number"
    print "So ", (delta/nums)/NUM_NODES, "sec per num per node"
