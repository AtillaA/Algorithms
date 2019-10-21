# Use the following commands to download the packages:
# python -m pip install matplotlib numpy scipy
# See https://docs.scipy.org/doc/numpy-1.15.1/user/quickstart.html for a comprehensive numpy tutorial.
# This tutorial aims to introduce you to the basics of statistical analysis in Python, which you will be using in your projects.

from timeit import default_timer as timer
import random
import copy
import matplotlib.pyplot as plt
import scipy as sp
from scipy.stats import t
from numpy.polynomial.polynomial import polyfit

def bubbleSort(alist): #O(n^2) sorting algorithm
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

#Create a random list with first n elements then 2n then 4n ...
#Then iterate over bubblesort algorithm for 5 times and get the average execution time
n = 125
cnt = 1
results_bub = []
results_pyt = [] 
iter = 5
while n <= 4000 :
    time_bub = 0.0
    time_pyt = 0.0
    for k in range(iter) :
        arr_bub = []
        for i in range(n) :
            num = random.randrange(0, n)
            arr_bub.append(num)
        arr_pyt = copy.deepcopy(arr_bub)
      
        start = timer()
        bubbleSort(arr_bub)
        end = timer()
        time_bub += end - start

        start = timer() 
        arr_pyt.sort()
        end = timer()
        time_pyt += end - start

    results_bub.append(time_bub / iter)
    results_pyt.append(time_pyt / iter)
    n *= 2
    print("end of iter : ", cnt)
    cnt += 1

ns = [125, 250, 500, 1000, 2000, 4000]
plt.plot(ns, results_bub, linewidth = 2.0)
plt.xlabel('Input size')
plt.ylabel('Running time (s)')
plt.show()

plt.plot(ns, results_pyt, linewidth = 2.0)
plt.xlabel('Input size')
plt.ylabel('Running time (s)')
plt.show()

print(results_bub)
print(results_pyt)