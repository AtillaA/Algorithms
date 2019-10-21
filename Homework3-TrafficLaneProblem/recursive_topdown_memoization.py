# Atilla Alpay Nalcaci - 19510
# HW3 Traffic Lane Problem - Recursive Algorithm with Memoization

import random
import time


# Variables
#---------------------------BEGIN---------------------------#
rowloc = int(input("Enter the row of the car: "))   # car must start at row 0
laneloc = int(input("Enter the lane of the car: "))  # car must start at lane 1
init = laneloc
n = int(input("Enter a row number: "))
map = [[0 for i in range(3)] for j in range(n)]  # matrix of size 'map[n][3]'
randint = random.randint(0, 2)  # random integer between 0-2
#----------------------------END----------------------------#


def print_matrix(A) :
    for i in range (len(A)):
        for k in range (len(A[0])):
            print(A[i][k],end=" ")
        print("\n")
    print("----------END----------\n")


# Roadmap matrix creation
#---------------------------BEGIN---------------------------#
def roadway(n):
    rmp = [[0 for i in range(3)] for j in range(n)]

    for i in range(len(rmp)):
        z = random.randint(0, 2)			# defining here so that at each loop a random variable will be generated

        while i == rowloc and z == laneloc:	# to ensure that there are no obstacles at the location of the car
            z = random.randint(0, 2)

        rmp[i][z] = 1

        for k in range(3):
            if k != z:
                rmp[i][k] = 0

    return rmp
#----------------------------END----------------------------#


# Memoization matrix creation
#---------------------------BEGIN---------------------------#
def memoization(n):
    data = [[0 for i in range(3)] for j in range(n)]

    for i in range(len(data)):
        for k in range(len(data[0])):
            data[i][k] = -1

    return data
#----------------------------END----------------------------#

map = roadway(n)        # define a variable for roadmap
table = memoization(n)  # define a variable for memoization matrix

print("--------ROADWAY--------\n")
print_matrix(map)
print("------MEMOIZATION------\n")
print_matrix(map)


# Main function (Recursive Algorithm with Memoization)
#---------------------------BEGIN---------------------------#
def TrafficLaneMemoization(row, lane, map, table):
    # print(row, lane)

    if row == len(map):
        return 0

    elif table[row][lane] != -1:
        return table[row][lane]

    elif map[row][lane] == 1:
        return 100

    else:
        if lane - 1 > 0 and lane + 1 < len(map[0]):
            table[row][lane] = min(TrafficLaneMemoization(row + 1, lane - 1, map, table) + 1, TrafficLaneMemoization(row + 1, lane, map, table), TrafficLaneMemoization(row + 1, lane + 1, map, table) + 1)

        elif lane - 1 < 0:
            table[row][lane] = min(TrafficLaneMemoization(row + 1, lane, map, table), TrafficLaneMemoization(row + 1, lane + 1, map, table) + 1)

        else:
            table[row][lane] = min(TrafficLaneMemoization(row + 1, lane - 1, map, table) + 1, TrafficLaneMemoization(row + 1, lane, map, table))

    return table[row][lane]
#----------------------------END----------------------------#


# Program initiate
#---------------------------BEGIN---------------------------#
timer_start = time.time()               # timer variable for calculating the running time of the algorithm
final = TrafficLaneMemoization(rowloc, laneloc, map, table)
timer_end = time.time()                 # stop the timer

print("Number of path changes:", final)                                        # will output 1 most of the time since algorithm aims to minimize lane changes
print("Running time of the Recursive Algorithm with Memoization:", (timer_end - timer_start))      # subtract the timer values to estimate the running time
# ----------------------------END----------------------------#