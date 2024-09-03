import sys

file_name = sys.argv[1]
with open(file_name, 'r') as file:
    nums = [int(line.strip()) for line in file]
nums.sort()
median = nums[len(nums) // 2]
count = 0
for num in nums:
    count += abs(num - median)
print(count)
