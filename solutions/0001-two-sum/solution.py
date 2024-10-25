'''
The One-pass Hash Table algorithm efficiently finds two numbers in a list that add up to a target value. 
It iterates through the list once, storing each number's index in a hash table. 
For each number, it checks if the complement (target - number) exists in the hash table, 
indicating that the two numbers sum to the target.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Initialize a dictionary to store numbers and their indices
        numIndexMap = {}

        # Iterate over the list of numbers
        for index, num in enumerate(nums):

            # Calculate the complement of the current number
            complement = target - num

            # Check if the complement is already in the dictionary
            if complement in numIndexMap:
                # If found, return the indices of the two numbers
                return [numIndexMap[complement], index]

            # Store the index of the current number in the dictionary
            numIndexMap[num] = index

        # Return an empty list if no solution is found (though the problem guarantees a solution)
        return []
