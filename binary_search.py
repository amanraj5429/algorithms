def binary_search(arr, l, r, x):
    while l<=r:
        mid = l + (r-l)//2
        if arr[mid] == x:
            return mid
        elif arr[mid]<x:
            l = mid+1
        else:
            r = mid-1
    return -1

if __name__ == '__main__':
    arr = [10,23,44,53,66]
    x = 13
    result = binary_search(arr, 0, len(arr)-1, x)
    print(result)
    