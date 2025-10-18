#списки з даними
nums = [4, 6, 100, 5.23, 0]
nums[0] = 69.9
#print(nums[3])

nums2 = [2, 1, 22, [7, "LOVE", True]]
#print(nums2[-2])

nums.append(45)
nums.insert(1,False)
#nums.extend(nums2)
nums.sort()
nums.reverse()
nums.pop()
nums.remove(5.23)
#nums.clear()


print(nums)
print(nums.count(0))
print(len(nums))