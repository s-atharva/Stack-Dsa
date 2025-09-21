from collections import deque

nums = [1, 3, 2, 4]
arr = []
stack = deque()

for i in range(len(nums) - 1, -1, -1):
    if not stack:
        arr.append(-1)
    elif stack and stack[-1] > nums[i]:
        arr.append(stack[-1])
    else:
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if not stack:
            arr.append(-1)
        else:
            arr.append(stack[-1])
    stack.append(nums[i])

# mutable
arr.reverse()
print(arr)


# stack = []
# stack.append(1)
# stack.append(2)
# stack.append(3)
#
# print(stack)
# stack.pop()
# print(stack)
