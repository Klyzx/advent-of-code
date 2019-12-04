def ref(arr, num, layer):
    if layer == 0:
        return arr[num]
    return ref(arr, arr[num], layer-1)

def opcod(arr, layers):
    i = 0
    while i < len(arr) and arr[i] != 99:
        if arr[i] == 1:
            arr[arr[i+3]] = ref(arr, i+1, layers) + ref(arr, i+2, layers)
        if arr[i] == 2:
            arr[arr[i+3]] = ref(arr, i+1, layers) * ref(arr, i+2, layers)
        if (arr[i] != 1) and (arr[i] != 2):
            return -1
        i += 4
    return arr[0]
