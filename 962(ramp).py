nums = [9,8,1,0,1,9,4,0,4,1]
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

############################ IF TIME LIMIT EXCEEDED ####################################