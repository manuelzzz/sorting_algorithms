def bubbleSort(aList):
    for passnum in range(len(aList) - 1, 0, - 1):
        for i in range(passnum):
            if aList[i] > aList[i+1]:
                temp = aList[i]
                aList[i] = aList[i+1]
                aList[i+1] = temp


x = [1,4,5,2,3,2,5]

print(x)
bubbleSort(x)
print(x)