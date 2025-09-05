def f(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return(i, j)
    return None
target = 6
nums = [3, 3, 3, 3]
print(f(nums, target))

