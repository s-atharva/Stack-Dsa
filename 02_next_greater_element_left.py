from typing import List


def nge_left(nums: List[int], n: int) -> List[int]:
    ans = []
    for i in range(n):
        greater = -1
        for j in range(i - 1, -1, -1):
            if nums[j] > nums[i]:
                greater = nums[j]
                break
        ans.append(greater)
    return ans


nums = [1, 3, 2, 4]
print(nge_left(nums=nums, n=len(nums)))
