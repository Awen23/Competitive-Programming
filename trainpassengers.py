#Solution to https://open.kattis.com/problems/trainpassengers

#getting the data from the input
nums = input().split()
stations = []

for x in range(0, int(nums[1])):
    stations.append(input().split())

#Tracking the amount of people on the train, then checking if it's one of the three impossible cases
#   1. There's a negative number of people on the train
#   2. There's more than the max people on the train
#   3. There's less than the max but someone waited for the next train
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

#if it gets here then it hasn't found an impossible case then quit, so it's possible
print("possible")
