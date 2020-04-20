# https://www.hackerrank.com/challenges/migratory-birds/problem

def migratoryBirds(arr):
    lookup = [0] * (max(arr) + 1)

    for birdType in arr:
        lookup[birdType] += 1

    birdType = 1
    maximumSighting = lookup[1]
    for i, sighting in enumerate(lookup[2:], 2):
        if sighting > maximumSighting:
            maximumSighting = sighting
            birdType = i

    return birdType
