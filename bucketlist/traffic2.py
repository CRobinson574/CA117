#!/usr/bin/env python3

import sys

def main():
    tokens = []

    for line in sys.stdin:
        line = line.strip()

        tokens.append(line)

    L = int(tokens[0])

    time = 0
    for line in tokens[1:]:
        D, R, G = line.split()

        #D, R, G = num[0], num[1], num[2]
        #print(D, R, G)

        extra = 0

        #cycle = (D + extra) % (R + G)
        #if cycle < R:
        #    time = time + R - cycle
        #    extra = extra + R - cycle
    time = L + extra
    print(time)

if __name__ == "__main__":
    main()
