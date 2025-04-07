
import itertools
import random
import sys
sys.stdin = open("test.in", "r")
sys.stdout = open("test.out", "w")

L, N , rf, rb = [int(x) for x in input().split()]


"""
High level solution:
Go to the stops that are higher than any other before it.just go to the one with the highest, so start search from the right, since we would just go that one. chances are we dont go to an earlier one

""" 

sys.stdin = open("test.in", "r")
sys.stdout = open("test.out", "w")

L, N, rf, rb = [int(x) for x in input().split()]

stops = []
for _ in range(N):
    stops.append([int(x) for x in input().split()])

# Sort stops by position
stops.sort(key=lambda x: x[0])


def simulate(L, stops, rf, rb):
    # Select only the stops that are worth stopping at.
    # We iterate from the end and pick stops with tastiness greater than all seen so far.
    optimal_stops = []
    max_taste = 0
    for x, c in reversed(stops):
        if c > max_taste:
            max_taste = c
            optimal_stops.append((x, c))
    # Reverse to process them in increasing order of position.
    optimal_stops.reverse()

    total_tastiness = 0
    prev_position = 0
    wait_time_per_meter = rf - rb  # extra seconds Bessie has per meter

    for x, c in optimal_stops:
        # The extra time Bessie gets to wait at this rest stop is the distance
        # from the previous rest stop times wait_time_per_meter.
        total_tastiness += (x - prev_position) * wait_time_per_meter * c
        prev_position = x

    return total_tastiness


print(simulate(L, stops, rf, rb))





    

        



    

