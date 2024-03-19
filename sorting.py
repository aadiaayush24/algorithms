
def selection_sort(arr: list):
    for i in range(len(arr) - 1):
        min = arr[i]
        minPos = i
        for j in range(i + 1, len(arr)):
            if (arr[j] < min):
                min = arr[j]
                minPos = j

        if (i != minPos):
            temp = arr[i]
            arr[i] = arr[minPos]
            arr[minPos] = temp

    return arr

def merge_sort(arr: list):
    def merge(left, right):
        array = []
        l, r = len(left), len(right)
        i, j = 0, 0
        while (i < l) and (j < r):
            if left[i] <= right[j]:
                array.append(left[i])
                i += 1
            else:
                array.append(right[j])
                j += 1
        while i < l:
            array.append(left[i])
            i += 1

        while j < r:
            array.append(right[j])
            j += 1

        return array
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[0:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        arr[:] = merge(left, right)
    return arr


