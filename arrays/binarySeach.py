def populateArray(n):
    arr = [i for i in range(n + 1)]
    return arr


def binarySearch(arr, num):
    # length check, if array length is less than 1, return None
    if len(arr) < 1:
        return None

    # declare low and high
    low = 0
    high = len(arr) - 1

    # loop, while low less than or equal to high
    while low <= high:
        # set guess to middle, between low and high
        mid = (low + high) // 2
        print(
            "Searching for: {num}, Low: {low}, Mid: {mid}, High: {high}".format(
                num=num, low=low, mid=mid, high=high
            )
        )
        # if num == arr[mid], return mid index
        if num == arr[mid]:
            return mid

        # if num was smaller than mid, set high as mid-1
        if num < arr[mid]:
            high = mid - 1
            print("New high: {high}".format(high=high))
        # else (guess was larger than mid), set low as mid+1
        else:
            low = mid + 1
            print("New low: {low}".format(low=low))

    # num not found
    return None


arr = populateArray(50)
print(binarySearch(arr, 27))
