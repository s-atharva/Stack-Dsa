nums = [1, 3, 2, 4]
stack = []
n = len(nums)
ans = []

for i in range(n - 1, -1, -1):
    if len(stack) == 0:
        ans.append(-1)
    elif len(stack) > 0 and stack[-1] > nums[i]:
        ans.append(stack[-1])
    else:
        while len(stack) and stack[-1] <= nums[i]:
            stack.pop()
        if len(stack):
            ans.append(stack[-1])
        else:
            ans.append(stack[-1])
    stack.append(nums[i])


ans.reverse()
print(ans)
