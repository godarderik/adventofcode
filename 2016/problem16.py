a = list("01110110101001000")
disk_length = 35651584
while len(a) < disk_length:
    out = a + ["0"]
    count = 0
    out += ["0" if x == "1" else "1" for x in reversed(a)]
    a = out

a = a[:disk_length]

while len(a) % 2 == 0:
    out = ""
    for k in xrange(0,len(a),2):
        out += "1" if a[k] == a[k+1] else "0"
    a = out
print a

