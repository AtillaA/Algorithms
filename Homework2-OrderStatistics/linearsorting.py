import matplotlib.pyplot as plt
import math
from timeit import default_timer as timer
import random
import statistics


def binarySearch_iterative(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpoint = int((first + last) / 2)
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


#recursive
def binarySearch(alist,item):
    if len(alist) ==  0:
       return False
    else:
        midpoint = int(len(alist)/2)
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
            else:
                return binarySearch(alist[midpoint+1:],item)


def binarySearch_improved(elem, arr, start, end):
    if start > end:
        return False
    mid = (start + end)//2
    if arr[mid] == elem:
        return mid
    elif arr[mid] > elem:
        # recursion to the mid-left
        return binarySearch_improved(elem, arr, start, mid - 1)
    else:
        # recursion to the mid-right
        return binarySearch_improved(elem, arr, mid + 1, end)
        
   
arr_4 = []
arr_5 = []
arr_6 = []
arr_7 = []

for i in range(1, (10**4 + 1)):
    arr_4.append(i)
for j in range(1, (10**5 + 1)):
    arr_5.append(j)
for k in range(1, (10**6 + 1)):
    arr_6.append(k)
for l in range(1, (10**7 + 1)):
    arr_7.append(l)

all = [arr_4, arr_5, arr_6, arr_7]
x_axis = []
bin_ite = []
bin_rec = []
bin_rec_imp = []


count = 1
mean_ite = []
mean_rec = []
mean_imp_rec = []


smth = []
time_3 = 0

std_dev_ite = []
std_dev_rec = []
std_dev_imp_rec = []

for i in all:
    x_axis.append(len(i))
    time_1 = 0
    time_2 = 0
    for j in range(50):
        key = random.randint(0, len(i))

        start = timer()
        hold = binarySearch_iterative(i, key)
        end = timer()
        time_1 += end - start
        mean_ite.append(time_1)

        start = timer()
        val = binarySearch(i, key)
        end = timer()
        time_2 += end - start
        mean_rec.append(time_2)

        start = timer()
        smth = binarySearch_improved(key, i, 0, len(i))
        end = timer()
        time_3 += end - start
        mean_imp_rec.append(time_3)

    print("End of iteration: ", count)
    bin_ite.append(time_1 / 50)
    bin_rec.append(time_2 / 50)
    bin_rec_imp.append(time_3 / 50)
    
    print(bin_rec_imp[count - 1] < bin_ite[count - 1])
    count += 1
    std_dev_ite.append(statistics.stdev(mean_ite))
    std_dev_rec.append(statistics.stdev(mean_rec))
    std_dev_imp_rec.append(statistics.stdev(mean_imp_rec))

plt.plot(x_axis, bin_ite, linewidth=1.5, color="orange")
plt.xlabel('Input size')
plt.ylabel('Running time (s)')
plt.title("Iterative version")
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.show()

plt.plot(x_axis, bin_rec, linewidth=1.5, color="purple")
plt.xlabel('Input size')
plt.ylabel('Running time (s)')
plt.title("Recursive version")
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.show()

plt.plot(x_axis, bin_rec_imp, linewidth=1.5, color="purple")
plt.xlabel('Input size')
plt.ylabel('Running time (s)')
plt.title("Improved recursive version")
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.show()

print("Std dev Iterative: ", std_dev_ite)
print("Std dev recursive: ", std_dev_rec)

print("Iterative: ", bin_ite)
print("Recursive: ", bin_rec)
print("Improved recursive: ", bin_rec_imp)
