arr = '.' + '.^^.^.^^^^' + '.'
count = arr.count('.') - 2

for x in range(40): 
    arr = "." + "".join(['^' if arr[k-1] != arr[k+1] else '.' for k,v in enumerate(arr) if k > 0 and k < len(arr) - 1]) + "."
    count += arr.count('.') - 2

print count 