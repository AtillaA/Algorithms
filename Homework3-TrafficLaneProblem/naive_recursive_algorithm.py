# Atilla Alpay Nalcaci - 19510
# HW3 Traffic Lane Problem - Naive Recursive Algorithm

import random
import time

# Variables
# ---------------------------BEGIN---------------------------#
rowloc = 0  # car must start at row 0
laneloc = 1  # car must start at lane 1
n = int(input("Enter a row number: "))
map = [[0 for i in range(3)] for j in range(n)]  # matrix of size 'map[n][3]'
randint = random.randint(0, 2)  # random integer between 0-2


# ----------------------------END----------------------------#

def print_matrix(A):
    for i in range(len(A)):
        for k in range(len(A[0])):
            print(A[i][k], end=" ")
        print("\n")
    print("----------END----------\n")


# Roadmap matrix creation
# ---------------------------BEGIN---------------------------#
for i in range(len(map)):
    x = random.randint(0, 2)  # defining here so that at each loop a random variable will be generated

    while x == laneloc and i == rowloc:  # to ensure that there are no obstacles at the location of the car
        x = random.randint(0, 2)

    map[i][x] = 1

    for a in range(3):
        if a != x:
            map[i][a] = 0
# ----------------------------END----------------------------#

print_matrix(map)


# Main function (Naive Recursive Algorithm)
# ---------------------------BEGIN---------------------------#
def TrafficLaneRecursive(row, lane, map):  # naive recursive function for the traffic lane problem
    # print(row, lane)

    if row == len(map) or len(map) == 0:  # meaning that our initial row is the final row in which case program terminates
        return 0

    elif map[row][lane] == 1:  # if the location (namely [0][1]) is occupied in which case the car cannot be inserted
        return 100

    else:
        if lane + 1 < len(map[0]) and lane - 1 > 0:
            return min(TrafficLaneRecursive(row + 1, lane - 1, map) + 1, TrafficLaneRecursive(row + 1, lane, map), TrafficLaneRecursive(row + 1, lane + 1, map) + 1)

        elif lane == 0:
            return min(TrafficLaneRecursive(row + 1, lane, map), TrafficLaneRecursive(row + 1, lane + 1, map) + 1)

        else:
            return min(TrafficLaneRecursive(row + 1, lane - 1, map) + 1, TrafficLaneRecursive(row + 1, lane, map))
# ----------------------------END----------------------------#


# Program initiate
# ---------------------------BEGIN---------------------------#
while map[n - 1][randint] != 1:
    randint = random.randint(0, 2)

timer_start = time.time()  # timer variable for calculating the running time of the algorithm
final = TrafficLaneRecursive(rowloc, laneloc, map)  # indicates the final position (of lane) of the car
timer_end = time.time()  # stop the timer

print("Number of path changes:", final)  # will output 1 most of the time since algorithm aims to minimize lane changes
print("Running time of the Naive Recursive Algorithm:",
      (timer_end - timer_start))  # subtract the timer values to estimate the running time
# ----------------------------END----------------------------#