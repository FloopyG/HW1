import random
import datetime

# Task 1

numSpace = 2
print(numSpace, "The number of keys in the 8-bit sequence: ", numSpace ** 8)
print(numSpace, "The number of keys in the 16-bit sequence: ", numSpace ** 16)
print(numSpace, "The number of keys in the 32-bit sequence: ", numSpace ** 32)
print(numSpace, "The number of keys in the 64-bit sequence: ", numSpace ** 64)
print(numSpace, "The number of keys in the 128-bit sequence: ", numSpace ** 128)
print(numSpace, "The number of keys in the 256-bit sequence: ", numSpace ** 256)
print(numSpace, "The number of keys in the 512-bit sequence: ", numSpace ** 512)
print(numSpace, "The number of keys in the 1024-bit sequence: ", numSpace ** 1024)
print(numSpace, "The number of keys in the 2048-bit sequence: ", numSpace ** 2048)
print(numSpace, "The number of keys in the 4096-bit sequence: ", numSpace ** 4096)


# Task 2

def key_generator(bits):
    bit_key = random.getrandbits(bits)
    hex_key = hex(bit_key)
    return hex_key


print("Random key using 8-bit sequence:", key_generator(8))
print("Random key using 16-bit sequence:", key_generator(16))
print("Random key using 32-bit sequence:", key_generator(32))
print("Random key using 64-bit sequence:", key_generator(64))
print("Random key using 128-bit sequence:", key_generator(128))
print("Random key using 256-bit sequence:", key_generator(256))
print("Random key using 512-bit sequence:", key_generator(512))
print("Random key using 1024-bit sequence:", key_generator(1024))
print("Random key using 2048-bit sequence:", key_generator(2048))
print("Random key using 4096-bit sequence:", key_generator(4096))


# Task 3

def key_bruteforce(key):
    bits = 2 ** ((len(key) - 2) * 4)
    print(bits)
    i = 0
    while i < bits:
        if hex(i) == key:
            print(key)
            print(hex(i))
            print("Success")
            break
        i += 1


start_time = datetime.datetime.now()

key_bruteforce(key_generator(16))

end_time = datetime.datetime.now()
time_diff = (end_time - start_time)
execution_time = time_diff.total_seconds() * 1000

print(execution_time, "ms")
