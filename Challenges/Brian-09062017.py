import sys

# Default provided function name from Hackerrank
def getTotalX(a, b):
    # Counter for total number of values in between sets
    total = 0

    # Expected range of values
    for val in range(1,101):
        # Flag to see if all lists are traversed
        lastx = 0
        lasty = 0

        # First loop to see if all val % a_i == 0 if so set flagx
        for x in a:
            if val % x == 0:
                if x == a[-1]:
                    lastx = 1
                continue
            else:
                break

        # Second loop to see if all b_i % val == 0 if so set flagy
        for y in b:
            if y % val == 0:
                if y == b[-1]:
                    lasty = 1
                continue
            else:
                break

        # Check if both flags are set to verify val satifies in between
        if lastx == 1 and lasty == 1:
            total += 1

    # Return the total count
    return total
        
# Default main funtion call from Hackerrank
if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = map(int, raw_input().strip().split(' '))
    b = map(int, raw_input().strip().split(' '))
    total = getTotalX(a, b)
    print total
