import sys

# Power of Google
#from collections import Counter

# I have this here to show what it's like to google something very short and clean code using libraries
"""
def migratoryBirds(n, ar):
    return Counter(ar).most_common(1)[0][0]
"""

def migratoryBirds(n, ar):
    # Number of different types of birds
    types = 5

    # Hashmap initialization to store values. We're given that based on number of types of birds
    dictionary = {}
    for bird in range(1, types+1):
        dictionary[str(bird)] = 0
        
    # Iterate through list to count the amount of birds
    for bird in ar:
        dictionary[str(bird)] += 1

    # First occurance saved and will compare against the rest
    maxOccurance = dictionary["1"]
    
    # Current leader
    result = "1"

    # Compare the rest of the items in the map to see which has the most
    for item in range(2, types+1):
        if dictionary[str(item)] > maxOccurance:
            maxOccurance = dictionary[str(item)]
            result = str(item)

    return result

if __name__ == "__main__":
    n = int(raw_input().strip())
    ar = map(int, raw_input().strip().split(' '))
    results = migratoryBirds(n, ar)
    print results
