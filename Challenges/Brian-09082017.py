def circularArrayLoop(self, nums):
    
    # N time to loop through "starting indexes"
    for x in range(len(nums)):

        """
        start: Determines the start of the potential loop
        direction: Flag to decide forward/backward direction
        index: Current index to compart to start
        counter: Checks if you've iterated at least once
        checked: Amount of indexes checked. If greater than len(nums), break
        """
        start = x
        direction = 0
        index = x
        counter = 0
        checked = 0

        # Checks the direction at the start index
        if nums[x] > 0:
            direction = 1
        else:
            direction = -1
        
        # Checked every index again (Another N so a total of O(N^2))
        while True:
            if checked > len(nums):
                break

            # Increment the counters/index
            index = (index+nums[index])
            counter += 1
            checked += 1
                
            # Checks if you go past the border of the list to wrap around
            if index > len(nums)-1:
                index = index-len(nums)
            elif index < 0:
                index = index+len(nums)

            # Checks to see if you change direction thus automatically failing
            if direction == 1 and nums[index] < 0:
                break
            elif direction == -1 and nums[index] > 0:
                break  

            # Checks to see if you fully connected the loop and is greater than 1 otherwise break
            if index == start and counter <= 1:
                break
            elif index == start and counter > 1:
                return True
        
    return False

if __name__ == "__main__":
    n = int(raw_input().strip())
    nums = map(int, raw_input().strip().split(' '))
    results = circularArrayLoop(nums)
    print results
