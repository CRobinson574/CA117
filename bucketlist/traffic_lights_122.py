#!/usr/bin/env python3

'''
Program that calculates the time it will take a cyclist to travel a road of L km containing traffic lights at any position along the road,
given that their speed is 1km/h
Date: 09/04/21
Author: Craig Robinson
'''

import sys

class TrafficLight(object):
    def __init__(self, D, R, G):
        '''Traffic light object that takes in D, the distance from the start, R the amount of time the light is red for, and G the time the light is Green for'''
        self.D = D
        self.R = R
        self.G = G

def main():
    tokens = []

    # Read the input and add to tokens to split up later
    for line in sys.stdin:
        line = line.strip()

        tokens.append(line)

    # L is the total distance of the road which is at tokens[0]
    L = int(tokens[0])

    # initialising the total time and the extra time for calculations
    time = 0
    extra = 0

    # iterating through the rest of the input which tells the position and timing of the traffic lights
    for line in tokens[1:]:

        D, R, G = line.split()
        tl = TrafficLight(int(D), int(R), int(G))

        #this calculates the time in the cycle that the person arrives at the light
        cycle = (tl.D + extra) % (tl.R + tl.G)

        # if the time in the cycle is less than the time the red light is on do this:
        if cycle < tl.R:
            time = time + tl.R - cycle
            extra = extra + tl.R - cycle

    # printing the output which is the length of the road + the extra time in this case
    time = L + extra
    print(time)

if __name__ == "__main__":
    main()
