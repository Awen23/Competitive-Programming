inp = input().split()
noSections = int(inp[0])
time = int(inp[1])
dist = []
speeds = []

for x in range(noSections):
    thisSection = input().split()
    dist.append(int(thisSection[0]))
    speeds.append(int(thisSection[1]))

testTime = -1
minC = 0 - min(speeds)
maxC = 1001000

while round(minC,6) != round(maxC,6):
    testTime = 0
    midC = (minC + maxC) / 2
    for x in range(noSections):
        testTime += (dist[x]/(speeds[x] + midC))

    if testTime > time:
        minC = midC
    elif testTime < time:
        maxC = midC
    else:
        maxC = minC

print('%.6f'%minC)
