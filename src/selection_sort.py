def selection_sort(aList):  
    length = len(aList)  
    for i in range(length - 1):  
        minIndex = i  
        for j in range(i + 1, length):
            if aList[j] < aList[minIndex]:
                minIndex = j
        aList[i], aList[minIndex] = aList[minIndex], aList[i]
    return aList
