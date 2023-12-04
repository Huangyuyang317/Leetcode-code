class Solution(object):
    def twoSum(self,nums,target):
        sol=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    sol.append(i)
                    sol.append(j)
                    return (sol)
###采用遍历算法