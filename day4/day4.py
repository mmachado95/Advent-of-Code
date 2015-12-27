import hashlib


def mining(secret_key):
    counter = 1
    magic_number1 = -1
    magic_number2 = -1
    key = secret_key + str(counter)

    while True:
        digest = hashlib.md5(key.encode('utf-8')).hexdigest()
        # First part of the problem
        if magic_number1 == -1 and digest[0:5] == '00000':
            magic_number1 = counter
        # Second part of the problem
        if magic_number2 == -1 and digest[0:6] == '000000':
            magic_number2 = counter
        if magic_number1 != -1 and magic_number2 != -1:
            break
        else:
            counter += 1
            key = secret_key + str(counter)
    print(magic_number1)
    print(magic_number2)


if __name__ == '__main__':
    mining('ckczppom')