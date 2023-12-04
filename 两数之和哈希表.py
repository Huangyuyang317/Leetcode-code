class Solution:
    def twoSum(self, nums:list[int], target: int) -> list[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []

            
    
s=input()
s1=list(map(int,s[1:][:-1].split(",")))
target=int(input())
m=Solution()
print(m.twoSum(s1,target))

###只需要O(N)