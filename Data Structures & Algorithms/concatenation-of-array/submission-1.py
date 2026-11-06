class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0] * (2*length)
        

        for i,number in enumerate(nums):
            answer[i] = answer[length + i] = nums[i]

        return answer        