# Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list. 


nums = [1, 3, 5, 7, 9, 11]

def binary_search(lis, item):
    low = 0
    high = len(lis) - 1

    while low <= high:
        mid = (low + high) // 2

        if lis[mid] == item:
            return mid

        elif lis[mid] < item:
            low = mid + 1

        else:
            high = mid - 1

    return -1 
print(binary_search(nums, 7))  