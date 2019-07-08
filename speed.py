#Getting details from inputs
inp = input().split()
noSections = int(inp[0])
time = int(inp[1])
dist = []
speeds = []
for x in range(noSections):
    thisSection = input().split()
    dist.append(int(thisSection[0]))
    speeds.append(int(thisSection[1]))

#Setting variables - minimum possible is what makes minimum speed 0
#   maximum possible is maxC (10^6) + maxSpeed (1000) as a speed could be -1000
testTime = -1
minC = 0 - min(speeds)
maxC = 1001000

#Rounded for speed, doing binary search for correct value
while round(minC,6) != round(maxC,6):
    testTime = 0
    midC = (minC + maxC) / 2
    for x in range(noSections):
        #calculating time with this c through time = dist/speed for all values
        testTime += (dist[x]/(speeds[x] + midC))

    if testTime > time:
        minC = midC
    elif testTime < time:
        maxC = midC
    else:
        maxC = minC

print('%.6f'%minC)
