
nums = [9,8,1,0,1,9,4,0,4,1]
'''
ramp = []
max = 0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[j] >= nums[i]:
            ramp.append((i,j))
for i in range(len(ramp)):
    if ramp[i][1] - ramp[i][0] > max:
        max = ramp[i][1] - ramp[i][0]
print(max)

###################### IF MEMORY LIMIT EXCEEDED ################################################

ramp = []
max = 0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[j] >= nums[i]:
            if j-i > max:
             max = j - i
print(max)
'''
############################ IF TIME LIMIT EXCEEDED ####################################
nums = [9,8,1,0,1,9,4,0,4,1]
n = len(nums)
indices = [i for i in range(n)]
print(indices)
# Sort indices based on corresponding values in nums and ensure stability
indices.sort(key=lambda i: (nums[i], i))
print(indices)

i = n  # Minimum index encountered so far
max_width = 0

# Calculate maximum width ramp
for j in indices:
    if j - i > max_width:
        max_width = j - i
    #max_width = max(max_width, i - min_index)
    #min_index = min(min_index, i)
    i = min(i, j)

print(max_width)