nums = input().split()
stations = []

for x in range(0, int(nums[1])):
    stations.append(input().split())

peopleOnTrain = 0
maxPeople = int(nums[0])
for stat in stations:
    peopleOnTrain -= int(stat[0])
    if peopleOnTrain < 0:
        print("impossible")
        quit()

    peopleOnTrain += int(stat[1])
    
    if peopleOnTrain > maxPeople:
        print("impossible")
        quit()

    if peopleOnTrain < maxPeople:
        if int(stat[2]) > 0:
            print("impossible")
            quit()

if peopleOnTrain > 0:
    print("impossible")
    quit()
    
print("possible")
