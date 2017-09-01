import sys

def main():
    # While loop to check if input is valid
    while(1):
        # Try/Except statement for raw_input return
        try:
            # Prompt to tell user to input value then break out of while
            val = int(raw_input("Please input a positive integer: ").strip())
            break
        except:
            # Except invalid input error and prompts again
            print "Invalid input, try again."
            continue
    
    # Construction of the staircase
    for step in xrange(val):
        # Variable to reduce redundancy
        breakpoint = val-step-1

        # Creates the spaces for the step
        for space in range(0, breakpoint):
            sys.stdout.write(' ')

        # Creates the actual steps using "#"
        for pound in range(breakpoint, val):
            sys.stdout.write('#')

        #Print new line for next step
        print ""

# Basic main method call in python if running as a stand alone program
if __name__ == "__main__": main()
