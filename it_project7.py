

nums = [True, "5", 7, [1, 22, False], not True, 25]
print(nums)
nums[0] = not nums[0]
print(nums[-1])
print(nums[3][1])
nums.append("првыт")
nums.insert(1, True)
print(nums)
nums.remove(True)
nums.reverse()
print(nums)
nums.pop()
print(nums.count(False))
nums.clear()
print(nums)





numbrs = list(range(20, 41))

for e in numbrs:
    e = e * (e**3 - 1)
    print(e)
