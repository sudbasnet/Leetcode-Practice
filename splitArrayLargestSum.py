class Solution:
    def splitArray(self, nums: [int], m: int) -> int:
        """
        One of the solutions that I can think of is by considering multiple options
        but here, the branches could be too large. For example, I cant just consider 
        every possibility, that would be absurd.
        
        how about we sum up everything and save the running sum first
        [7,2,5,10,8]
        runningSums = [7, 9, 14, 24, 32]
        
        say we take 7 then remaining woul be 32 - 7 = 25
        say we take 9 so we got left 23
        say we take 14, so we got left with 18 ???
        
        not sure how to do it!!!
        
        might need to look at the hints
        """