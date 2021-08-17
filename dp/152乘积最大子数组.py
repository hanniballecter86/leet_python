"""
给你一个整数数组 nums，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
------------------------------------------------
解题思路
由于任意位置的乘积最大的连续子数组都与前一位置相关，即存在重复的子结构，因此可以使用动态规划进行求解。
状态转移方程的推导：
    由于数组内的数字可正、可负，正的时候可以使用fmax(i) = max(fmax(i-1) * nums[i], fmin(i-1) * nums[i], nums[i])进行求解，
    负的时候则应该使用fmax(i) = max(fmax(i-1) * nums[i], fmin(i-1) * nums[i], nums[i])进行求解，因此应该维护两个状态方程fmax
    和fmin。
算法流程：
    1. 初始化pre_fmax、pre_fmin和res，使其均等于nums[0]；
    2. 从位置1开始遍历，分别计算每一个位置对应的cur_fmax和cur_fmin，0不需要额外操作，其会自动置零；
    3. 更新res，更新pre_max，pre_min；
    4. 重复2，3直到遍历完所有数字；
    5. 返回res的值
"""
class Solution:
    def maxProduct(self, nums) -> int:
        if not nums: return
        res, pre_max, pre_min = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            cur_max = max(pre_max * nums[i], pre_min * nums[i], nums[i])
            cur_min = min(pre_max * nums[i], pre_min * nums[i], nums[i])
            res = max(res, cur_max)
            pre_max, pre_min = cur_max, cur_min
        return res
    
result = Solution()
res = result.maxProduct([-4,-3,-2])
print(res)
            