from hashlib import md5
thecode = 'yzbqklnj'
integer = 0
while 1:
    result = md5((thecode + str(integer)).encode()).hexdigest()
    str(result)
    if result[:5] == '00000':  # change to result[:6] == '000000' for part 2
        print(result)
        print(integer)
        break
    integer += 1
