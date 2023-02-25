# Find smallest value's index by iterating through each array item
def findSmallest(arr):
    smallestIndex = 0
    for i in range(len(arr)):
        if arr[smallestIndex] > arr[i]:
            smallestIndex = i
    return smallestIndex


# Not in-place
def selectionSort1(arr):
    newArr = []
    for i in range(len(arr)):
        # find smallest value index
        smallestIndex = findSmallest(arr)
        # append smallest value to new array and pop it from the original array
        newArr.append(arr.pop(smallestIndex))
    return newArr


# In-place
def selectionSort2(arr):
    for i in range(len(arr)):
        # find smallest value index from arr, ignoring values before i, that have already been sorted
        smallestIndex = findSmallest(arr[i:])
        # swap the current index array value with the smallest index array value. Adjust positioning of smallest index based on number of iterations.
        arr[i], arr[smallestIndex + i] = arr[smallestIndex + i], arr[i]
    return arr


print(selectionSort1([65, 22, 1, 8, 17, 99]))
print(selectionSort2([65, 22, 1, 8, 17, 99]))
