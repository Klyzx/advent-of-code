from hashlib import md5
thecode = 'yzbqklnj'
integer = 0

def hash(num):
    global integer
    global thecode
    while True:
        result = md5((thecode + str(integer)).encode()).hexdigest()
        str(result)
        if result[:num] == '0'*num:
            print(result)
            print(integer)
            break
        integer += 1

hash(5)
hash(6)
