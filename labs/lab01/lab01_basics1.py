def quick(arr, first, last, dr):
    i = first
    j = last
    pivot = first
    while (1):
        if dr == 'rl':  # scan from right to left to find an element smaller than pivot
            while arr[pivot] <= arr[j] and pivot != j:
                j = j - 1
            if pivot == j:  # stop if scanning crosses pivot index
                dr = 'nn'
            if arr[pivot] > arr[j]:  # Interchange pivot element and smaller element on right
                temp = arr[j]
                arr[j] = arr[pivot]
                arr[pivot] = temp
                pivot = j
                dr = 'lr'  # change direction of scanning
            continue
        if dr == 'lr':  # scan from left to right to find an element bigger than pivot
            while arr[pivot] >= arr[i] and pivot != i:
                i = i + 1
            if pivot == i:  # stop if scanning crosses pivot index
                dr = 'nn'
            if arr[pivot] < arr[i]:  # Interchange pivot element and bigger element on left
                temp = arr[i]
                arr[i] = arr[pivot]
                arr[pivot] = temp
                pivot = i
                dr = 'rl'  # change direction of scanning
            continue
        if dr == 'nn':
            break
    return pivot  # return correct position of pivot element


def quicksort(arr, num):
    beg = 0
    end = 0
    mid = 0
    top = 0
    # initialise stacks to store sublist stast and end indices
    lower = []
    upper = []
    # push array boundaries
    lower.append(0)
    upper.append(num - 1)
    while (top != -1):
        # pop boudaries of a sublist
        beg = lower.pop()
        end = upper.pop()
        top = top - 1
        # call quick to place first element at correct position and get it indes
        mid = quick(arr, beg, end, 'rl')
        # create sublists by excluded correctly placed pivot element
        if (beg < mid - 1):
            # push left sublist boundaries
            lower.append(beg)
            upper.append(mid - 1)
            top = top + 1
        if (mid + 1 < end):
            # push right sublist boundaries
            lower.append(mid + 1)
            upper.append(end)
            top = top + 1


# display data of the array
def disparr(arr, n):
    i = 0
    print("Array elements are--->")
    while (i < n):
        print(arr[i])
        i = i + 1


arrlist = []
n = 0
t = 0
n = int(input("Number of elements you want to add--->"))
while (t < n):
    arrlist.append(int(input("input value--->")))
    t = t + 1
print("Before Sorting:")
disparr(arrlist, n)
quicksort(arrlist, n)
print("After Sorting:")
disparr(arrlist, n)
