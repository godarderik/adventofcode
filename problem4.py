import hashlib

key = "ckczppom"


def problema():
    num = 0
    while True:
        val = hashlib.md5(key + str(num)).hexdigest()
        if val[:5] == "00000":
            return num
        num += 1
def problemb():
    num = 0
    while True:
        val = hashlib.md5(key + str(num)).hexdigest()
        if val[:6] == "000000":
            return num
        num += 1
print problema(), problemb()