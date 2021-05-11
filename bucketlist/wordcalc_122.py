#!/usr/bin/env python3

import sys

def calc(words, tokens):
    ''' Function to calculate the variables and return the answers'''

    # just the tokens needed for calculation
    clean_tokens = tokens[1:len(tokens) - 1]

    # single string of the tokens needed
    s = " ".join(clean_tokens)

    # loop replaces variables for the numbers they represent
    # returns unkown if any variable is not in the dictionary
    for i in clean_tokens:
        if i in words.keys():
            s = s.replace(i, words[i])

        elif i != "+" and i != "-":
            sout = " ".join(clean_tokens) + " = unknown"
            return sout

    # making a new dictionary that is the reverse of the original, i.e:
    # {foo : 3} becomes {3 : foo}
    d = {}
    for k, v in words.items():
        d[v] = k

    # evaluating the string created earlier and keeping is as type str
    seval = str(eval(s))

    # checking if the answer is mapped to a variable and printing the correct variable if it does
    # prints unknown if not
    if seval in words.values():
        sout = " ".join(clean_tokens) + " = " + d[seval]
        return sout
    else:
        sout = " ".join(clean_tokens) + " = unknown"
        return sout


def main():
    words = {}
    for line in sys.stdin:
        tokens = line.strip().lower().split()

        # creates the dictionary
        if "def" in tokens:
            var, num = tokens[1], tokens[2]
            words[var] = num

        # calculates the equation
        elif "calc" in tokens:
           print(calc(words, tokens))

        # clears the dictionary
        elif "clear" in tokens:
            words.clear()

if __name__ == "__main__":
    main()
