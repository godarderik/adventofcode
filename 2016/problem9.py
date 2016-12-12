def get_length(inpt):
    status = 0
    ind = 0
    count2 = 0
    temp = ""
    while ind < len(inpt):
        char = inpt[ind]
        if char == "(":
            temp = ""
            status = 1
        elif status == 1 and char != ")":
            temp += char
        elif status == 1 and char == ")": 
            temp = [int(x) for x in temp.split("x")]
            count2 += get_length(inpt[ind+1: ind + temp[0]+1]) * temp[1]
            ind += temp[0]
            status = 0
        else:
            count2 += 1
        ind += 1
    return count2


with open ("input9.txt") as f:
    for line in f:
        line = line.strip()
        print get_length(line)

