from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        l = []
        for i in d:
            if d[i]>len(nums)//3:
                l.append(i)
        return l