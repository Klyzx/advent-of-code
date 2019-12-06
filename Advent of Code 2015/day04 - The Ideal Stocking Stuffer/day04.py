from hashlib import md5
thecode = 'yzbqklnj'


def hash(num):
    integer = 0
    while True:
        result = md5((thecode + str(integer)).encode()).hexdigest()
        if result[:num] == '0'*num:
            return(integer)
        integer += 1


print(hash(5))
print(hash(6))
