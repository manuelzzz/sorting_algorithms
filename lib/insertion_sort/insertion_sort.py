def insertionSort(aList):
    for index in range(1, len(aList)):
        currentValue = aList[index]
        position = index

        while position > 0 and aList[position - 1] > currentValue:
            aList[position] = aList[position - 1]
            position = position - 1
            
        aList[position] = currentValue

x = [4, 90, 4, 3, 32]

print(x)
insertionSort(x)
print(x)