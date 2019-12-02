def opcod(arr):
    i = 0
    while i < len(arr) and arr[i] != 99:
        if arr[i] == 1:
            arr[arr[i+3]] = arr[arr[i+1]] + arr[arr[i+2]]
        if arr[i] == 2:
            arr[arr[i+3]] = arr[arr[i+1]] * arr[arr[i+2]]
        if (arr[i] != 1) and (arr[i] != 2):
            return -1
        i += 4
    return arr[0]
