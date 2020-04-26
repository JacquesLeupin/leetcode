def twoSum(nums, target):
	mapper = {}
	for i, c in enumerate (nums):
		rest = target - c
		if rest in mapper:
			return [i, mapper[rest]]
		else:
			mapper[c] = i 
twoSum([2,7,11,15], 9)
