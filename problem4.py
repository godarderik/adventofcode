import hashlib

key = "ckczppom"

num = 0
while True:
    val = hashlib.md5(key + str(num)).hexdigest()
    if val[:6] == "000000":
        print num
        break
    num += 1