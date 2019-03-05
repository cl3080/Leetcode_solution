class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = len(nums)
        freq = collections.defaultdict(int)
        for num in nums:
            freq[num] = freq[num] + 1
            if freq[num] > size/2:
                return num
