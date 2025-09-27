from typing import List


def nge_left_brute(nums: List[int], n: int) -> List[int]:
    answer = []
    for i in range(n):
        number = -1
        for j in range(i - 1, -1, -1):
            if nums[j] > nums[i]:
                number = nums[j]
                break
        answer.append(number)
    return answer


def nge_left_stack(nums: List[int], n: int) -> List[int]:
    my_stack = []
    answer = []
    for i in range(n):
        if len(my_stack) == 0:
            answer.append(-1)
        elif my_stack[-1] > nums[i] and len(my_stack):
            answer.append(my_stack[-1])
        else:
            while len(my_stack) > 0 and my_stack[-1] <= nums[i]:
                my_stack.pop()
            if len(my_stack) == 0:
                answer.append(-1)
            else:
                answer.append(my_stack[-1])
        my_stack.append(nums[i])
    return answer


nums = [1, 3, 2, 4]
print(nge_left_brute(nums=nums, n=len(nums)))
print(nge_left_stack(nums=nums, n=len(nums)))
