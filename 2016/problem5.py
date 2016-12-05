import hashlib

key = "ojvtpuvg"

t = [-1]*8
num = 0
out = ""

while True:
    val = hashlib.md5(key + str(num)).hexdigest()
    if val.startswith("00000"):
        out += val[5]
        try:
            k = int(val[5])
            if k >= 8:
                pass
            elif t[k] == -1:
                t[k] = val[6]
            print t
        except:
            pass
    num += 1
    if all([z != -1 for z in t]):
        break
print out[:8], ["".join(t)][0]
