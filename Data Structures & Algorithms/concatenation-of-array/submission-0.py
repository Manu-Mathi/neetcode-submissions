class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(2):
            for number in nums:
                answer.append(number)
        
        return answer
        