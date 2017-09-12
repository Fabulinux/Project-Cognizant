class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2:
            return False
        
        direction = 0
        for x in range(len(nums)):
            start = x
            index = x
            counter = 0
            if nums[x] > 0:
                direction = 1
            else:
                direction = -1
            visited = []
            while True:
                if len(visited) > len(nums):
                    break
                index = (index+nums[index])
                counter += 1
                
                if index > len(nums)-1:
                    index = index-len(nums)
                elif index < 0:
                    index = index+len(nums)

                if direction == 1 and nums[index] < 0:
                    break
                elif direction == -1 and nums[index] > 0:
                    break  
                if index == start and counter <= 1:
                    break
                elif index == start and counter > 1:
                    return True
                visited.append(1)
        
        return False
