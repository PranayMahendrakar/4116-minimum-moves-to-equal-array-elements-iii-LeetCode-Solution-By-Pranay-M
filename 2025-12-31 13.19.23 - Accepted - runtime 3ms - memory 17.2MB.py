class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # All elements should become the maximum
        max_val = max(nums)
        return sum(max_val - num for num in nums)