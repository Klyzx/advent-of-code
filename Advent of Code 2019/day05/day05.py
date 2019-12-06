nums = open('input05.txt').read().split(',')
for i in range(len(nums)):
    nums[i] = int(nums[i])


def opcode(arr):
    i = 0
    while i < len(arr):
        if arr[i] == 99:
            print("stop")
            break
        opcode = arr[i] % 100
        if opcode in [1, 2, 5, 6, 7, 8]:
            modea = arr[i]//100 % 10
            modeb = arr[i]//1000 % 10

            if modea == 1:
                a = arr[i + 1]
            else:
                a = arr[arr[i + 1]]
            if modeb == 1:
                b = arr[i + 2]
            else:
                b = arr[arr[i + 2]]

            if opcode == 1:
                arr[arr[i + 3]] = a + b
                i += 4
            if opcode == 2:
                arr[arr[i + 3]] = a * b
                i += 4
            if opcode == 5:
                if a != 0:
                    i = b
                    continue
                else:
                    i += 3
            if opcode == 6:
                if a == 0:
                    i = b
                    continue
                else:
                    i += 3
            if opcode == 7:
                if a < b:
                    arr[arr[i + 3]] = 1
                else:
                    arr[arr[i + 3]] = 0
                i += 4
            if opcode == 8:
                if a == b:
                    arr[arr[i + 3]] = 1
                else:
                    arr[arr[i + 3]] = 0
                i += 4
            continue
        if opcode in [3, 4]:
            if opcode == 4:
                print(arr[arr[i + 1]])
            if opcode == 3:
                x = int(input("Num: "))
                arr[arr[i + 1]] = x

            i += 2
            continue


opcode(nums)
