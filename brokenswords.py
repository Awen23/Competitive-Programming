#Getting number of sticks
num = int(input())
numTB = 0
numLR = 0

#Going through each stick checking how many of each type of piece is available
for x in range(num):
    thisStick = list(input())

    if(thisStick[0] == '0'):
        numTB += 1

    if(thisStick[1] == '0'):
        numTB += 1
        
    if(thisStick[2] == '0'):
        numLR += 1

    if(thisStick[3] == '0'):
        numLR += 1

#Possible number of sticks is minimum of both, then divided by 2 as 2 used for each stick
#   int used as we want to round down, then calc remaining sticks for both    
numSticks = int( min(numTB, numLR) / 2)
remTB = numTB - (numSticks * 2)
remLR = numLR - (numSticks * 2)
print("{} {} {}".format(numSticks, remTB, remLR))
